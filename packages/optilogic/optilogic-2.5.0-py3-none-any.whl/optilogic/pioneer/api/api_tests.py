'''
This module performs unit tests on the Pioneer REST API

Usage:
  api_tests.py [--authlegacy=<bool>] [--user=<str>] [--pass=<str>] [--appkey=<str>] [--wksp=<str>]
  api_tests.py (-h | --help)

Examples:
  api_tests.py --user=username --pass=secret
  api_tests.py --user=username --appkey=op_guid --wksp=sqa

Options:
  -h, --help
  -a, --authlegacy=<bool>  true for legacy username password method [default: False]
  -u, --user=<str>         API user [default:]
  -p, --pass=<str>         API password [default:]
  -k, --appkey=<str>       non expiring auth key [default:]
  -w, --wksp=<str>         wksp to use [default: Studio]
'''

import api
import os
import time
import unittest
from contextlib import redirect_stderr, redirect_stdout
from dateutil.parser import parse
from datetime import date, datetime, timedelta
from docopt import docopt
from io import StringIO
from json import dumps, loads
from numbers import Number
from random import randint
from re import fullmatch, search
from sys import platform
from typing import Any, Dict, List, Literal, Tuple, Optional
from warnings import warn
from uuid import uuid4


class TestApi(unittest.TestCase):
    '''A series of Pioneer REST API unit tests

    OVERRIDE
    docopt configuration passed into the module will override the default static members

    STATIC MEMBERS
    USERNAME    required to be issued api key
    USERPASS    required to be issued api key
    WKSP        file storage to use for IO operations
    APPKEY      non expiring authentication key
    AUTH_LEGACY true for legacy username password authentication method
    '''

    USERNAME: Optional[str] = None
    USERPASS: Optional[str] = None
    WKSP: str = 'Studio'
    APPKEY: Optional[str] = None
    AUTH_LEGACY: bool = False

    # method execution order - unittest.TestLoader.sortTestMethodsUsing
    # default string sort of class method names startswith test_{method-name}, ie dir(self)

    @classmethod
    def setUpClass(cls) -> None:
        '''called before test methods are ran
        ensure cache directories and test data inputs are available in target wksp
        '''

        cls.API = api.Api(
            auth_legacy=cls.AUTH_LEGACY,
            appkey=cls.APPKEY,
            un=cls.USERNAME,
            pw=cls.USERPASS,
        )
        cls.__jobkey_quick: str = ''
        cls.API._log_active = True

        # directory references
        cls.dir_local_current: str = os.path.dirname(__file__)
        cls.dir_testdata_local: str = os.path.join(cls.dir_local_current, 'quick_tests')
        assert os.path.exists(cls.dir_testdata_local)
        assert len(os.listdir(cls.dir_testdata_local)) >= 1
        cls.dir_testdata_remote: str = 'quick_tests'
        cls.files_testdata_local: list[str] = []
        cls.files_testdata_remote: list[str] = []
        cls.py_run_me: str = ''
        cls.py_run_me_bash: str = ''
        cls.py_run_me_quick: str = ''

        # get all directories from wksp
        resp = cls.API.wksp_files(cls.WKSP, '/quick_tests/')
        files_remote: list[str] = [f['filePath'] for f in resp['files']]

        # comb over local test data and map to destination file structure
        for f in os.listdir(cls.dir_testdata_local):
            local: str = os.path.join(cls.dir_testdata_local, f)
            if os.path.isfile(local) is False:
                continue
            elif os.path.getsize(local) == 0:
                continue
            dest: str = os.path.join(cls.dir_testdata_remote, f)
            cls.files_testdata_local.append(local)
            cls.files_testdata_remote.append(dest)
            if dest.endswith('sleep.py'):
                cls.py_run_me = dest
            elif dest.endswith('quick.py'):
                cls.py_run_me_quick = dest
            elif dest.endswith('bash.py'):
                cls.py_run_me_bash = dest

            # upload local test data to destination
            for idx, local in enumerate(cls.files_testdata_local):
                dest = cls.files_testdata_remote[idx]
            res: list[str] = [f for f in files_remote if dest in f]
            if len(res) == 0:
                print(f'uploading {dest}')
                resp = cls.API.wksp_file_upload(
                    cls.WKSP, file_path_dest=dest, file_path_local=local
                )

    def database_ensure_exist(self, name: str = 'pg_unittest') -> None:
        '''database must exist for db unit tests'''

        # cache is for 10 seconds
        exists: bool = self.API.storagename_database_exists(name)
        if exists:
            resp: Dict[str, Any] = self.API.storage(name)
            assert resp.get('crash') is None
        else:
            self.API.database_create(name, desc='common db for unit tests')

    def date_isoformat(self, date_str: str) -> bool:
        '''is date string isoformat'''

        d: date
        try:
            d = date.fromisoformat(date_str)
            return isinstance(d, date)
        except ValueError:
            return False

    def job_prereq(self) -> None:
        '''for running test methods in isolation'''

        resp = self.API.wksp_job_start(
            self.WKSP, self.py_run_me_quick, tags='unittest_prereq', resourceConfig='mini'
        )
        self.assertEqual(resp['result'], 'success')
        self.__jobkey_quick = resp['jobKey']
        # BUG ledger and metrics should be immediately available when job is running
        res: bool = self.API.util_job_monitor(self.WKSP, resp['jobKey'], stop_when='done')
        self.assertTrue(res)

    def storage_common(self, d: Dict[str, Any]) -> None:
        '''common keys across afs, wksp, onedrive, and postgres storage devices'''

        self.assertIsInstance(d['annotations'], dict)
        # self.assertIsInstance(d['bytesUsed'], int) # BUG OE-7949 OneDrive
        self.assertTrue(d['bytesUsed'] is None or isinstance(d['bytesUsed'], int))
        self.assertIsInstance(d['created'], int)
        self.assertTrue(d['description'] is None or isinstance(d['description'], str))
        self.assertIsInstance(d['id'], str)
        self.assertIsInstance(d['labels'], dict)
        self.assertTrue(d['lockoutReason'] is None or isinstance(d['lockoutReason'], str))
        self.assertIsInstance(d['name'], str)
        self.assertIsInstance(d['notes'], str)
        self.assertIsInstance(d['tags'], str)
        self.assertIsInstance(d['type'], str)
        self.assertIsInstance(d['updated'], int)

    def storage_azure_afs(self, d: Dict[str, Any]) -> None:
        '''common ssd response for get device and devices'''

        self.storage_common(d)
        self.assertIsInstance(d['capacity'], int)
        self.assertIsInstance(d['internal'], bool)
        self.assertIsInstance(d['tier'], str)

    def storage_azure_workspace(self, d: Dict[str, Any]) -> None:
        '''common wksp response for get device and devices'''

        self.storage_common(d)
        self.assertIsInstance(d['capacity'], int)
        self.assertIsInstance(d['internal'], bool)
        self.assertIsInstance(d['tier'], str)
        self.assertIsInstance(d['workspaceKey'], str)

    def storage_database(self, d: Dict[str, Any]) -> None:
        '''common db response for get device and devices'''

        self.storage_common(d)
        self.assertIsInstance(d['bytesUsedLastUpdated'], int)
        self.assertIsInstance(d['dbname'], str)
        self.assertIsInstance(d['defaultSchema'], str)
        self.assertIsInstance(d['host'], str)
        self.assertIsInstance(d['port'], int)
        self.assertIsInstance(d['schemaStatus'], str)
        self.assertTrue(d['schemaStatus'] in ('error', 'invalid', 'valid'))
        # self.assertIsInstance(d['schemaStatusLastUpdated'], float)  # BUG OE-7561
        self.assertIsInstance(d['schemaVersion'], str)
        self.assertIsInstance(d['user'], str)
        # empty pg datase vs anura schema
        if d['defaultSchema'].startswith('anura_2_'):
            self.assertRegex(d['schemaVersion'], r'2\.[4-9]\.\d+')
            # self.assertIsInstance(d['schemaStatusLastValidated'], float)  # BUG OE-7561
        else:
            # self.assertTrue(len(d['defaultSchema']) == 0)  # TODO OE-7561
            self.assertTrue(len(d['schemaVersion']) == 0)

    def storage_onedrive(self, d: dict) -> None:
        '''common onedrive storage response for get device and devices'''

        self.storage_common(d)
        self.assertIsInstance(d['accountName'], str)
        self.assertIsInstance(d['authenticated'], int)
        self.assertIsInstance(d['capacity'], int)
        self.assertIsInstance(d['created'], int)
        self.assertIsInstance(d['endpointSuffix'], str)
        self.assertIsInstance(d['homeAccountId'], str)
        self.assertIsInstance(d['internal'], bool)
        self.assertIsInstance(d['protocol'], str)
        self.assertIsInstance(d['userId'], str)
        self.assertIsInstance(d['username'], str)

    def test_000_init_api_version_bad(self) -> None:
        '''recover from a bad api version provided'''

        bad_version: int = 99

        with redirect_stderr(StringIO()) as err:
            a = api.Api(auth_legacy=self.AUTH_LEGACY, version=bad_version, ut=True)
            output: str = err.getvalue().strip()

        self.assertGreater(output.find(f'API version {bad_version} not supported'), -1)
        self.assertRegex(a.api_version, r'app/v0/')

    def test_000_init_password_missing(self) -> None:
        '''get password uses a secret stream and input will not echo'''

        if platform != 'linux':
            self.skipTest('only linux has timed inputs')

        with redirect_stdout(StringIO()) as out:
            try:
                a = api.Api(auth_legacy=True, un=self.USERNAME, ut=True)
            except (EOFError, TimeoutError):
                pass
            output: str = out.getvalue().strip()

        self.assertEqual(output.find('REQUIRED API User Password'), -1)

    def test_000_prereqs(self) -> None:
        '''ensure job data is available to test against'''

        resp = self.API.wksp_job_start(
            self.WKSP, self.py_run_me_quick, tags='unittest_preseed', resourceConfig='mini'
        )
        self.assertEqual(resp['result'], 'success')
        self.__jobkey_quick = resp['jobKey']
        stime: float = time.time()
        print('Pre-seeding by running a new job')
        res: bool = self.API.util_job_monitor(
            self.WKSP, resp['jobKey'], stop_when='done', secs_max=300
        )
        delta: float = time.time() - stime
        print(f'Job completed {res}, time spent {delta}')
        self.assertLessEqual(delta, 240.0)

    def test_auth_apikey(self) -> None:
        '''api key is required for all api calls with legacy authentication'''

        self.assertIsNotNone(
            self.API.auth_apikey
        ) if self.API.auth_method_legacy else self.assertIsNone(self.API.auth_apikey)

    def test_auth_apikey_expiration(self) -> None:
        '''ensure api key is refreshed and not expired'''

        if self.API.auth_method_legacy:
            self.assertGreater(self.API.auth_apikey_expiry, datetime.now().timestamp())
        else:
            self.assertEqual(self.API.auth_apikey_expiry, 0)

    def test_auth_header(self) -> None:
        '''request header must have valid apikey or appkey'''

        if self.API.auth_method_legacy:
            self.assertEqual(self.API.auth_req_header['x-api-key'], self.API.auth_apikey)
        else:
            self.assertEqual(self.API.auth_req_header['x-app-key'], self.API.auth_appkey)

    def test_account_info(self) -> None:
        '''account properties'''

        resp = self.API.account_info()
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp), 7)
        self.assertIsInstance(resp['email'], str)
        self.assertGreater(resp['email'].find('@optilogic.com'), -1)  # assume employee user
        self.assertIsInstance(resp['name'], str)
        self.assertGreaterEqual(len(resp['name']), 3)
        # TODO regex name validation
        self.assertIsInstance(resp['subscriptionName'], str)
        self.assertEqual(resp['subscriptionName'], 'empcustom')  # assume employee user

        self.assertIsInstance(resp['limits'], dict)
        self.assertEqual(len(resp['limits']), 3)
        self.assertIsInstance(resp['limits']['concurrentJobs'], int)
        self.assertIsInstance(resp['limits']['databaseCount'], int)
        self.assertIsInstance(resp['limits']['fileStorageGb'], int)
        self.assertEqual(resp['limits']['concurrentJobs'], 50)
        self.assertEqual(resp['limits']['databaseCount'], 100)
        self.assertEqual(resp['limits']['fileStorageGb'], 500)  # max possible

        self.assertIsInstance(resp['usage'], dict)
        self.assertEqual(len(resp['usage']), 5)
        self.assertIsInstance(resp['usage']['databaseCount'], int)
        self.assertIsInstance(resp['usage']['databaseStorageBytes'], int)
        dbs_total_bytes: int = resp['usage']['databaseStorageBytes']
        self.assertIsInstance(resp['usage']['fileStorageCount'], int)
        self.assertIsInstance(resp['usage']['fileStorageGb'], int)
        self.assertIsInstance(resp['usage']['workspaceCount'], int)
        self.assertGreaterEqual(resp['usage']['databaseCount'], 0)
        self.assertLessEqual(resp['usage']['databaseCount'], resp['limits']['databaseCount'])
        self.assertTrue(0 < resp['usage']['fileStorageCount'] < 10)
        self.assertTrue(0 < resp['usage']['workspaceCount'] < 10)
        self.assertLessEqual(
            resp['usage']['fileStorageGb'],
            resp['limits']['fileStorageGb'] * resp['usage']['fileStorageCount'],
        )

        self.assertIsInstance(resp['username'], str)
        if self.API.auth_username:
            self.assertEqual(resp['username'], self.API.auth_username)

        dbs: List[Dict[str, Any]] = self.API.databases()
        total: int = 0
        for db in dbs:
            total += db['bytesUsed']

        self.assertEqual(dbs_total_bytes, total)

    def test_account_jobs(self) -> None:
        ''' 'any user job from any workspace'''

        job_count: int = 50
        resp = self.API._account_jobs(max_jobs=job_count)
        self.assertIsInstance(resp['jobs'], list)
        self.assertIsInstance(resp['result'], str)
        self.assertIsInstance(resp['subsetCount'], int)
        self.assertIsInstance(resp['totalCount'], int)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['subsetCount'], job_count)
        for job in resp['jobs']:
            self.assertIsInstance(job['canHaveResult'], bool)
            self.assertIsInstance(job['jobInfo'], dict)
            self.assertIsInstance(job['jobInfo']['command'], str)
            if job['jobInfo']['command'] != 'run_custom':
                self.assertIsInstance(job['jobInfo']['directoryPath'], str)
                self.assertIsInstance(job['jobInfo']['filename'], str)
            self.assertIsInstance(job['jobInfo']['resourceConfig'], dict)
            self.assertIsInstance(job['jobInfo']['resourceConfig']['cpu'], str)
            self.assertIsInstance(job['jobInfo']['resourceConfig']['name'], str)
            self.assertIsInstance(job['jobInfo']['resourceConfig']['ram'], str)
            self.assertIsInstance(
                float(job['jobInfo']['resourceConfig']['run_rate']), float
            )  # BUG OE-6710 float or int
            self.assertIsInstance(job['jobInfo']['tags'], str)
            self.assertIsInstance(int(job['jobInfo']['timeout']), int)  # BUG OE-6710 str or int
            self.assertIsInstance(job['jobInfo']['workspace'], str)
            self.assertIsInstance(job['jobKey'], str)
            self.assertIsInstance(float(job['runRate']), float)  # BUG OE-6710 float or int
            self.assertIsInstance(job['status'], str)
            self.assertIsInstance(job['submittedDatetime'], str)
            self.assertIsInstance(job['submittedTimeStamp'], int)

            if job['status'] in ('done', 'cancelled', 'error'):
                self.assertTrue(job['canHaveResult'])
                self.assertIsInstance(job['billedTime'], str)
                self.assertIsInstance(float(job['billedTimeMs']), float)  # BUG OE-6710 float or int
                self.assertIsInstance(job['endDatetime'], str)
                self.assertIsInstance(job['endTimeStamp'], int)
                self.assertIsInstance(job['runTime'], str)
                self.assertIsInstance(job['runTimeMs'], int)
                self.assertIsInstance(job['startDatetime'], str)
                self.assertIsInstance(job['startTimeStamp'], int)
            else:
                # self.assertFalse(job['canHaveResult']) # BUG OE-6710 stopped cant have a result
                pass

    def test_account_jobs_active(self) -> None:
        '''compare active account jobs count to all active wksp jobs'''

        start_new_job: bool = bool(randint(0, 1))
        if start_new_job:
            self.API.wksp_job_start(
                self.WKSP, self.py_run_me, tags='unittest_jobs_active', resourceConfig='mini'
            )

        active_account: int = 0
        resp = self.API._account_jobs(
            max_jobs=200
        )  # BUG submitted counts as active therefore must account for excessive submitted jobs
        for job in resp['jobs']:
            if job['status'] in self.API.JOBSTATES_ACTIVE:
                active_account += 1

        active_wksp: int = self.API._jobs_active
        self.assertEqual(active_account, active_wksp)
        if start_new_job:
            self.assertGreater(active_account, 0)
            self.assertGreater(active_wksp, 0)

    def test_account_storage_devices(self) -> None:
        '''get a list of available storage devices in an account'''

        resp = self.API.account_storage_devices()
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['storages'], list)
        with self.subTest():
            for d in resp['storages']:
                if d['type'] == 'azure_afs':
                    self.assertEqual(len(d), 15)
                    self.storage_azure_afs(d)
                if d['type'] == 'azure_workspace':
                    self.assertEqual(len(d), 16)
                    self.storage_azure_workspace(d)
                elif d['type'] == 'onedrive':
                    self.assertEqual(len(d), 22)
                    self.storage_onedrive(d)
                elif d['type'] == 'postgres_db':
                    self.assertEqual(len(d), 22)
                    self.storage_database(d)

    def test_account_usage(self) -> None:
        '''atlas and andromeda information'''

        resp = self.API._account_usage()
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['andromeda'], dict)
        self.assertIsInstance(resp['atlas'], dict)
        self.assertEqual(len(resp), 3)

        self.assertIsInstance(resp['andromeda']['jobsLastThirty'], int)
        self.assertIsInstance(resp['andromeda']['jobsMostRecent'], int)
        self.assertIsInstance(resp['andromeda']['jobsTimeLastThirty'], float)
        self.assertIsInstance(resp['andromeda']['jobsTimeTotal'], float)
        self.assertIsInstance(resp['andromeda']['jobsTotal'], int)
        self.assertIsInstance(resp['andromeda']['periodHours'], float)
        self.assertEqual(len(resp['andromeda']), 6)
        self.assertEqual(len(str(resp['andromeda']['jobsMostRecent'])), 13)
        dt: datetime = datetime.fromtimestamp(resp['andromeda']['jobsMostRecent'] / 1000)
        now: datetime = datetime.utcnow()
        self.assertEqual(dt.year, now.year)
        self.assertEqual(dt.month, now.month)

        self.assertIsInstance(resp['atlas'], dict)
        self.assertIsInstance(resp['atlas']['lastLogin'], int)
        if resp['atlas']['periodHours'] == 0:
            self.assertIsInstance(resp['atlas']['periodHours'], int)
        else:
            self.assertIsInstance(resp['atlas']['periodHours'], float)
        self.assertIsInstance(resp['atlas']['task'], dict)
        self.assertIsInstance(resp['atlas']['workspaceCount'], int)
        self.assertEqual(len(resp['atlas']), 4)
        self.assertEqual(len(str(resp['atlas']['lastLogin'])), 13)
        dt: datetime = datetime.fromtimestamp(resp['atlas']['lastLogin'] / 1000)
        self.assertIsInstance(dt, datetime)

        self.assertIsInstance(resp['atlas']['task'], dict)
        if resp['atlas']['task']['durationCurrentWeek'] == 0:
            self.assertIsInstance(resp['atlas']['task']['durationCurrentWeek'], int)
        else:
            self.assertIsInstance(resp['atlas']['task']['durationCurrentWeek'], float)
        if resp['atlas']['task']['durationLastThirty'] == 0:
            self.assertIsInstance(resp['atlas']['task']['durationLastThirty'], int)
        else:
            self.assertIsInstance(resp['atlas']['task']['durationLastThirty'], float)
        self.assertIsInstance(resp['atlas']['task']['durationTotal'], float)
        self.assertIsInstance(resp['atlas']['task']['lastDuration'], float)
        self.assertIsInstance(resp['atlas']['task']['lastRunStart'], int)
        self.assertIsInstance(resp['atlas']['task']['runCurrentWeek'], int)
        self.assertIsInstance(resp['atlas']['task']['runlastThirty'], int)
        self.assertIsInstance(resp['atlas']['task']['runTotal'], int)
        self.assertEqual(len(resp['atlas']['task']), 8)
        self.assertEqual(len(str(resp['atlas']['task']['lastRunStart'])), 13)
        dt: datetime = datetime.fromtimestamp(resp['atlas']['task']['lastRunStart'] / 1000)
        self.assertIsInstance(dt, datetime)

    def test_account_workspaces(self) -> None:
        '''check all workspaces properties'''

        resp = self.API.account_workspaces()
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)

        wksp_exists: bool = False
        for wksp in resp['workspaces']:
            self.assertRegex(wksp['name'], '^[\\w-]+$')
            self.assertEqual(len(wksp['key']), 25)
            self.assertIn(wksp['stack'], ['Optilogic', 'Gurobi'])
            self.assertIn(wksp['status'], ['STARTING', 'RUNNING', 'STOPPING', 'STOPPED'])
            self.assertRegex(wksp['status'], '\\w{3,}')

            # https://en.wikipedia.org/wiki/ISO_8601
            dt_wksp_creation: datetime = parse(wksp['createdon'])
            self.assertGreaterEqual(dt_wksp_creation.year, 2020)

            if wksp['name'] == self.WKSP:
                wksp_exists = True

        self.assertTrue(wksp_exists)

    def test_account_workspace_count(self) -> None:
        '''account info and workspaces both return wksp count'''

        resp = self.API.account_info()
        ws_count: int = self.API.account_workspace_count
        self.assertEqual(resp['usage']['workspaceCount'], ws_count)

    @unittest.skip('cant delete a wksp atm')
    def test_account_workspace_create(self) -> None:
        '''creating a new workspace'''

        resp = self.API.account_workspace_create('delme')
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['name'], 'delme')
        self.assertEqual(resp['stack'], 'Gurobi')

    def test_account_workspace_create_crash(self) -> None:
        '''expected to not create the same workspace twice'''

        resp = self.API.account_workspace_create('Studio')
        self.assertEqual(resp['crash'], True)
        self.assertEqual(resp['exception'].response.status_code, 400)

    def test_account_workspace_delete(self):
        '''deleting a newly created workspace'''

        with self.assertRaises(NotImplementedError):
            resp = self.API.account_workspace_delete('delme')

    def test_api_server_online(self) -> None:
        '''check if api service is up and running'''

        self.assertTrue(self.API.api_server_online)

    def test_api_version(self) -> None:
        '''only version zero is supported'''

        self.assertTrue(self.API.api_version.endswith('v0/'))

    def test_database_create_delete(self) -> None:
        '''create a postgres database then delete'''

        bots: List[str] = self.API._database_templates_legacy_by_name('blast', wildcard=True)
        self.assertGreaterEqual(len(bots), 1)
        dbname: str = f'pg_unittest_{time.perf_counter_ns()}'

        # create database
        resp: dict = self.API.database_create(dbname, desc=f'unittest {dbname}', template=bots[0])
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['storageId'], str)
        self.assertEqual(len(resp['storageId']), 36)

        # verify database was created
        db_created: bool = False
        start: float = time.perf_counter()
        wait_until: float = 60.0
        while db_created is False and (time.perf_counter() - start) < wait_until:
            resp = self.API.database(dbname)
            if resp.get('crash'):
                continue
            if resp.get('result') == 'success':
                db_created = True
                break
            time.sleep(2)

        with self.subTest():
            self.assertTrue(db_created)

        if db_created is False:
            warn(f'failed to create db within {wait_until} seconds)', UserWarning, stacklevel=2)

        # delete database
        resp = self.API.storage_delete(dbname)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')

    def test_database_create_delete_wrong_id(self) -> None:
        '''create a postgres database with a template name instead of id'''

        tname: str = 'Out of China'
        self.assertFalse(tname in self.API.DATABASE_TEMPLATES)
        with self.assertRaises(ValueError):
            self.API.database_create(name='cant', template=tname)

        # get template id
        tids: List[str] = self.API._database_templates_legacy_by_name(tname)
        self.assertEqual(len(tids), 1)
        self.assertEqual(tids[0], 'b69f11eb-ed38-4b72-a43d-d59f7ab2cfa6')
        dbname: str = f'pg_unittest_{time.perf_counter_ns()}'

        # create database with matching template id
        resp = self.API.database_create(dbname, desc=f'unittest {dbname} {tname}', template=tids[0])
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['storageId'], str)
        self.assertEqual(len(resp['storageId']), 36)

        # verify database creation
        db = self.API.database(dbname)
        self.assertEqual(db['result'], 'success')
        self.assertEqual(db['name'], dbname)
        self.assertEqual(db['type'], 'postgres_db')
        self.assertEqual(db['id'], resp['storageId'])
        self.assertGreater(db['description'].find(tname), -1)

        # delete database
        resp = self.API.storage_delete(dbname)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')

    def test_database_create_failure_template_bad(self) -> None:
        '''attempt creating a postgres database with bad template id'''

        with self.assertRaises(ValueError):
            self.API.database_create(name='cant', template='does_not_exist')

    def test_database_create_failure_template_swap(self) -> None:
        '''attempt creating a postgres database with template name instead of id'''

        with self.assertRaises(ValueError):
            self.API.database_create(name='cant', template='Out of China')

    def test_database_objects(self) -> None:
        '''tables and views with stats'''

        self.database_ensure_exist()
        resp: Dict[str, Any] = self.API.database_objects('pg_unittest')
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['schemas'], list)
        for schema in resp['schemas']:
            self.assertEqual(len(schema.keys()), 6)
            self.assertIsInstance(schema['isDefault'], bool)
            self.assertIsInstance(schema['name'], str)
            self.assertIsInstance(schema['tableCount'], int)
            self.assertIsInstance(schema['tables'], list)
            self.assertIsInstance(schema['viewCount'], int)
            self.assertIsInstance(schema['views'], list)
            self.assertEqual(len(schema['tables']), schema['tableCount'])
            self.assertEqual(len(schema['views']), schema['viewCount'])
            for t in schema['tables']:
                self.assertIsInstance(t['name'], str)
                self.assertIsInstance(t['rows'], int)
                self.assertGreaterEqual(len(t['name']), 1)
                self.assertGreaterEqual(t['rows'], 0)

        # tables only
        resp: Dict[str, Any] = self.API.database_objects('pg_unittest', views=False)
        self.assertEqual(resp['result'], 'success')
        for schema in resp['schemas']:
            self.assertIsNone(schema.get('views'))

        # views only
        resp: Dict[str, Any] = self.API.database_objects('pg_unittest', tables=False)
        self.assertEqual(resp['result'], 'success')
        for schema in resp['schemas']:
            self.assertIsNone(schema.get('tables'))

    def test_database_schemas(self) -> None:
        '''currently only anura schemas'''

        ANURA_STATUS: Tuple[str, ...] = ('current', 'deprecated', 'preview', 'retired')
        resp = self.API.database_schemas()
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['schemas'], dict)
        self.assertEqual(len(resp), 2)
        self.assertEqual(len(resp['schemas']), 1)
        self.assertTrue(resp['schemas'].get('anura', False))
        for schema_type in resp['schemas'].keys():
            for v in resp['schemas'][schema_type]:
                self.assertEqual(len(v), 10)
                self.assertIsInstance(v['generalAvailabilityDate'], str)
                self.assertIsInstance(v['description'], str)
                self.assertIsInstance(v['notes'], str)
                self.assertIsInstance(v['schemaName'], str)
                self.assertRegex(v['schemaName'], r'anura_2_[4-9]')
                self.assertIsInstance(v['schemaVersion'], str)
                self.assertRegex(v['schemaVersion'], r'2\.[4-9]\.\d+')
                self.assertIsInstance(v['status'], str)
                self.assertIn(v['status'], ANURA_STATUS)
                self.assertTrue(self.date_isoformat(v['generalAvailabilityDate']))
                if v.get('defaultMigrationDate'):
                    self.assertIsInstance(v['defaultMigrationDate'], str)
                    self.assertTrue(self.date_isoformat(v['defaultMigrationDate']))
                if v.get('endOfLifeDate'):
                    self.assertIsInstance(v['endOfLifeDate'], str)
                    self.assertTrue(self.date_isoformat(v['endOfLifeDate']))
                if v.get('limitedAvailabilityDate'):
                    self.assertIsInstance(v['limitedAvailabilityDate'], str)
                    self.assertTrue(self.date_isoformat(v['limitedAvailabilityDate']))
                if v.get('techPreviewDate'):
                    self.assertIsInstance(v['techPreviewDate'], str)
                    self.assertTrue(self.date_isoformat(v['techPreviewDate']))

    def test_database_tables(self) -> None:
        '''list of schemas and tables'''

        self.database_ensure_exist()
        db = self.API.account_storage_device(type='postgres_db')
        resp = self.API.database_tables(db['name'])
        self.assertIsInstance(resp['result'], str)
        for schema in resp['schemas']:
            self.assertIsInstance(schema['name'], str)
            self.assertIsInstance(schema['tables'], int)
            self.assertIsInstance(schema['is_default_schema'], bool)
        self.assertIsInstance(resp['tables'], list)

        if len(resp['tables']) >= 1:
            self.assertIsInstance(resp['tables'][0]['name'], str)
            self.assertIsInstance(resp['tables'][0]['rows'], int)
            self.assertIsInstance(resp['tables'][0]['schema'], str)

    def test_database_tables_empty(self) -> None:
        '''clear the data in specified tables'''

        db: str = 'pg_unittest_empty_bom_table'
        tbl: str = 'billsofmaterials'
        anura_versions: list[str] = sorted(
            {t[0:9] for t in self.API.DATABASE_TEMPLATES if t.find('anura') > -1}, reverse=True
        )
        schema: str = anura_versions[0]

        # assert db exists
        exists: bool = self.API.storagename_database_exists(db)
        if exists:
            resp = self.API.storage(db)
            schema = resp['defaultSchema']
        else:
            self.API.database_create(name=db, template=f'{schema}_clean')

        # assert db has data
        QUERY_ROWS: str = f'SELECT COUNT(*) FROM {schema}.{tbl}'
        resp = self.API.sql_query(db, QUERY_ROWS)
        rows: int = int(resp['queryResults'][0]['count'])
        if rows == 0:
            query_insert = f'INSERT INTO {schema}.{tbl}\n'
            query_insert += (
                '(bomname, productname, producttype, quantity, quantityuom, status, notes)\n'
            )
            query_insert += f"VALUES\n('Unittest', 'RM1', 'Component', '1', 'EA', 'Exclude', 'unittest{time.time()}')"
            self.API.sql_query(db, query_insert)
            rows = 1

        # remove table data dry run
        resp = self.API.database_tables_empty(db, tables=[tbl], dry_run=True)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp), 4)
        self.assertTrue(resp['dryRun'])
        self.assertIsInstance(resp['emptied'], list)
        self.assertEqual(len(resp['emptied']), 1)
        self.assertEqual(resp['emptied'][0], f'{schema}.{tbl}')
        self.assertIsInstance(resp['failed'], list)
        self.assertEqual(len(resp['failed']), 0)
        resp = self.API.sql_query(db, QUERY_ROWS)
        rows_dry_run: int = int(resp['queryResults'][0]['count'])
        self.assertEqual(rows, rows_dry_run)

        # remove table data
        resp = self.API.database_tables_empty(db, tables=[tbl])
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp), 4)
        self.assertFalse(resp['dryRun'])
        self.assertIsInstance(resp['emptied'], list)
        self.assertEqual(len(resp['emptied']), 1)
        self.assertEqual(resp['emptied'][0], f'{schema}.{tbl}')
        self.assertIsInstance(resp['failed'], list)
        self.assertEqual(len(resp['failed']), 0)
        resp = self.API.sql_query(db, QUERY_ROWS)
        rows_cleared: int = int(resp['queryResults'][0]['count'])
        self.assertEqual(rows_cleared, 0)

    def test_database_templates(self) -> None:
        '''empty db or anura schemas'''

        resp: Dict[str, Any] = self.API.database_templates()
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp.keys()), 3)
        self.assertIsInstance(resp['count'], int)
        self.assertEqual(resp['count'], 14)
        self.assertIsInstance(resp['templates'], list)
        tcount: int = len(resp['templates'])
        self.assertEqual(tcount, 14)
        self.assertEqual(tcount, resp['count'])
        for t in resp['templates']:
            self.assertIsInstance(t, dict)
            for k in t.keys():
                self.assertIsInstance(k, str)

    def test_database_templates_legacy(self) -> None:
        '''legacy empty db or anura schemas'''

        resp: Dict[str, Any] = self.API._database_templates_legacy()
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertEqual(resp['count'], 15)  # TODO OE-7816
        self.assertIsInstance(resp['templates'], list)
        tcount: int = len(resp['templates'])
        self.assertEqual(tcount, 15)
        self.assertEqual(tcount, resp['count'])
        self.assertEqual(tcount, len(self.API.DATABASE_TEMPLATES) + 1)  # TODO OE-7816

        TEMPLATE_KEYS: Tuple[str, ...] = ('id', 'is_default', 'name', 'role', 'schema')
        for t in resp['templates']:
            self.assertIsInstance(t, dict)
            for k in t.keys():
                self.assertIsInstance(k, str)
            keys = tuple(sorted(t.keys()))
            # self.assertEqual(keys, TEMPLATE_KEYS) # TODO OE-7816
            # if t['name'] in ('Empty Database', 'Blast Off To Space (BOTS)', 'Global Risk Analysis'):
            #    continue  # OE-7918 legacy call changed
            # self.assertTrue(t['id'] in self.API.DATABASE_TEMPLATES)

    def test_database_templates_legacy_by_name(self) -> None:
        '''look up the database template id by case-insensitive template name'''

        template_names: List[str] = [
            'empty',
            'Anura - Blast off to Space',
            'Anura - New Model',
            'Anura - New Model (2.6)',
            'China Exit Strategy in Asia',
            'Detailed Facility Selection',
            'Fleet Size Optimization - EMEA Geo',
            'Fleet Size Optimization - US Geo',
            'Greenfield Facility Selection',
            'Multi-Year Capacity Planning',
            'Out of China',
            'Tactical Capacity Optimization',
        ]

        for name in template_names:
            tids: List[str] = self.API._database_templates_legacy_by_name(name)
            self.assertEqual(len(tids), 1)

    def test_ip_address_allow(self) -> None:
        '''whitelist ip address'''

        self.database_ensure_exist()
        db: Dict[str, Any] = self.API.account_storage_device(type='postgres_db')
        resp: Dict[str, str] = self.API.ip_address_allow(database_name=db['name'], ip='127.0.0.0')

        self.assertIsInstance(resp['ip'], str)
        self.assertIsInstance(resp['message'], str)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['ip'], '127.0.0.0')
        self.assertEqual(resp['result'], 'accepted')
        self.assertIn('five-minute delay', resp['message'])

    def test_ip_address_allow_invalid(self) -> None:
        '''unable to whitelist, ip address is invalid'''

        self.database_ensure_exist()
        db: Dict[str, Any] = self.API.account_storage_device(type='postgres_db')
        r: Dict[str, Any] = self.API.ip_address_allow(database_name=db['name'], ip='alpha.0.0.0')
        resp: dict = r['resp'].json()
        self.assertIsInstance(resp['message'], str)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['message'], 'ipAddress is missing or invalid')
        self.assertEqual(resp['result'], 'error')

    def test_ip_address_allowed(self) -> None:
        '''ip address is whitelisted'''

        self.database_ensure_exist()
        db: Dict[str, Any] = self.API.account_storage_device(type='postgres_db')
        resp: Dict[str, Any] = self.API.ip_address_allowed(database_name=db['name'], ip='127.0.0.0')
        self.assertIsInstance(resp['allowed'], bool)
        self.assertIsInstance(resp['ip'], str)
        self.assertIsInstance(resp['message'], str)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['allowed'], True)
        self.assertEqual(resp['ip'], '127.0.0.0')
        self.assertEqual(resp['result'], 'success')
        self.assertIn('is in the firewall', resp['message'])

    def test_ip_address_allowed_invalid(self) -> None:
        '''ip address is invalid'''

        self.database_ensure_exist()
        db: Dict[str, Any] = self.API.account_storage_device(type='postgres_db')
        r: Dict[str, Any] = self.API.ip_address_allowed(database_name=db['name'], ip='alpha.0.0.0')
        resp: dict = r['resp'].json()

        self.assertIsInstance(resp['message'], str)
        self.assertIsInstance(resp['result'], str)
        self.assertEqual(resp['message'], 'ipAddress is missing or invalid')

    def test_ip_address_is(self) -> None:
        '''identify external IP4 address'''

        ip: str = self.API.ip_address_is()
        pat = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$'
        valid_ip4 = bool(fullmatch(pat, ip))
        self.assertTrue(valid_ip4)
        ipq: str = self.API._ip_address_is_quick()
        self.assertEqual(ip, ipq)

    def test_onedrive_push(self) -> None:
        '''push optilogic files to onedrive'''

        with self.assertRaises(NotImplementedError):
            self.API.onedrive_push('fakeFilePath')

        return  # OE-7039 API: OneDrive Push Broke

        # does account even have onedrive storage?
        onedrive: bool = self.API.storagetype_onedrive_exists
        if onedrive is False:
            self.skipTest('OneDrive device not available')

        # storage device info cached, grab the first onedrive device name
        devices = self.API.account_storage_devices()
        onedrives = [d for d in devices['storages'] if d['type'] == 'onedrive']

        # upload a file to onedrive device
        file_contents: str = f'{datetime.now()} unittest test_onedrive_push {time.time()}'
        file_path: str = f"/{onedrives[0]['name']}/unittest.txt"
        self.API.wksp_file_upload('Studio', file_path, overwrite=True, filestr=file_contents)

        # initiate push to onedrive
        resp = self.API.onedrive_push(file_path)
        self.assertEqual(resp['result'], 'success')
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['storageId'], str)
        self.assertIsInstance(resp['storageName'], str)
        self.assertTrue(resp['storageId'], onedrives[0]['id'])
        self.assertTrue(resp['storageName'], onedrives[0]['name'])

    def test_secret_add(self) -> None:
        '''create a new secret'''

        nano_secs: str = str(time.perf_counter_ns())
        n: str = 'unittest_secret_last_added'
        prereq = self.API.secret(n)
        if prereq.get('crash'):
            self.API.secret_add(n, value=nano_secs, category='unittest')
        else:
            self.API.secret_update(n, value=nano_secs)

        cat: str = 'geocode'
        desc: str = f'unittest {nano_secs}'
        for provider in self.API.GEO_PROVIDERS:
            meta_dict: dict = {'isDefault': False, 'provider': provider}
            meta_str: str = dumps(meta_dict)
            name: str = f'ut_{provider}_{nano_secs}'
            value: str = str(uuid4())

            resp = self.API.secret_add(name, value, cat, desc, meta=meta_str)
            self.assertIsInstance(resp['created'], str)
            self.assertIsInstance(resp['description'], str)
            self.assertIsInstance(resp['id'], str)
            self.assertIsInstance(resp['meta'], str)
            self.assertIsInstance(resp['name'], str)
            self.assertIsInstance(resp['result'], str)
            self.assertIsInstance(resp['type'], str)
            self.assertIsInstance(resp['value'], str)
            self.assertEqual(resp['description'], desc)
            self.assertEqual(resp['meta'], meta_str)
            self.assertEqual(resp['name'], name)
            self.assertEqual(resp['result'], 'success')
            self.assertEqual(resp['type'], cat)
            self.assertEqual(resp['value'], value)
            self.assertTrue(resp['created'].endswith('Z'))
            dt: datetime = parse(resp['created'])
            self.assertTrue(dt.tzname(), 'UTC')
            now: datetime = datetime.utcnow()
            self.assertEqual(dt.year, now.year)
            self.assertEqual(dt.month, now.month)
            self.assertEqual(dt.day, now.day)

    def test_secret_alter(self) -> None:
        '''modify a secret'''

        secrets = self.API._secret_select_all(desc='unittest')  # no values returned, too sensitive
        sec: dict = {}
        name: str = ''
        for secret in secrets:
            if secret['name'].find('bing') > -1:
                sec = secret
                name = secret['name']
                break

        secret = self.API.secret(name)
        newname: str = 'ut_altered'

        resp = self.API.secret_update(name, new_name=newname)
        self.assertEqual(resp['created'], sec['created'])
        self.assertEqual(resp['id'], sec['id'])
        self.assertEqual(resp['description'], sec['description'])
        self.assertEqual(resp['meta'], sec['meta'])
        self.assertEqual(resp['name'], newname)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['type'], sec['type'])

        old = self.API.secret(name)
        self.assertTrue(old['crash'])
        d: dict = loads(old['response_body'])
        self.assertIsInstance(d, dict)
        self.assertEqual(d['result'], 'error')
        self.assertGreater(d['message'].find('no secret found'), -1)
        self.assertEqual(secret['value'], resp['value'])

        new = self.API.secret('ut_altered')
        self.assertEqual(resp['id'], new['id'])
        self.assertEqual(resp['name'], newname)

    def test_secrets(self) -> None:
        '''check all secrets'''

        resp = self.API.secrets()
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['secrets'], list)
        self.assertGreaterEqual(len(resp['secrets']), 1)

        for s in resp['secrets']:
            self.assertIsInstance(s['created'], str)
            self.assertEqual(len(s['created']), 24)
            self.assertIsInstance(s['id'], str)
            self.assertEqual(len(s['id']), 36)
            self.assertIsInstance(s['name'], str)
            self.assertGreater(len(s['name']), 0)

            if s.get('description'):
                self.assertIsInstance(s['description'], str)
            if s.get('meta'):
                self.assertIsInstance(s['meta'], str)
            if s.get('type'):
                self.assertIsInstance(s['type'], str)

            dt: datetime = parse(s['created'])
            self.assertTrue(dt.tzname(), 'UTC')

    def test_secrets_exist(self) -> None:
        '''check newly created unittest secrets'''

        prereq = self.API.secret('unittest_secret_last_added')
        if prereq.get('crash'):
            self.skipTest('must first run method test_secret_add')
        nano_secs: str = prereq['value']

        self.assertFalse(
            self.API._secret_exist(name='does_not_exist', category='geocode', desc='unittest')
        )
        self.assertFalse(
            self.API._secret_exist(
                name=f'ut_pcmiler_{nano_secs}', category='geocode', desc='does_not_exist'
            )
        )
        self.assertTrue(
            self.API._secret_exist(
                name=f'ut_pcmiler_{nano_secs}', category='geocode', desc='unittest'
            )
        )

        self.assertFalse(self.API._secret_exist(name='does_not_exist', category='geocode'))
        self.assertFalse(
            self.API._secret_exist(name=f'ut_pcmiler_{nano_secs}', category='does_not_exist')
        )
        self.assertTrue(self.API._secret_exist(name=f'ut_pcmiler_{nano_secs}', category='geocode'))

        self.assertFalse(self.API._secret_exist(name='does_not_exist', desc='unittest'))
        self.assertFalse(
            self.API._secret_exist(name=f'ut_pcmiler_{nano_secs}', desc='does_not_exist')
        )
        self.assertTrue(self.API._secret_exist(name=f'ut_pcmiler_{nano_secs}', desc='unittest'))

        self.assertFalse(self.API._secret_exist(category='geocode', desc='does_not_exist'))
        self.assertTrue(self.API._secret_exist(category='geocode', desc='unittest'))

        self.assertFalse(self.API._secret_exist(name='does_not_exist'))
        self.assertTrue(self.API._secret_exist(name=f'ut_pcmiler_{nano_secs}'))

        self.assertFalse(self.API._secret_exist(category='does_not_exist'))
        self.assertTrue(self.API._secret_exist(category='geocode'))

        self.assertFalse(self.API._secret_exist(desc='does_not_exist'))
        self.assertTrue(self.API._secret_exist(desc='unittest'))

    def test_secrets_remove(self) -> None:
        '''remove all unittest secrets'''

        secrets = self.API._secret_select_all(desc='unittest')

        for s in secrets:
            resp = self.API.secret_delete(s['name'])
            self.assertEqual(resp['result'], 'success')
            self.assertEqual(resp['id'], s['id'])
            self.assertEqual(resp['name'], s['name'])

    def test_sql_connect_info(self) -> None:
        '''get the connection information for a sql storage item'''

        self.database_ensure_exist()
        pg = self.API.account_storage_device('postgres_db')
        resp = self.API.sql_connection_info(pg['name'])
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp['raw']), 6)
        self.assertIsInstance(resp['raw']['host'], str)
        self.assertTrue(resp['raw']['host'].endswith('postgres.database.azure.com'))
        self.assertIsInstance(resp['raw']['dbname'], str)
        self.assertIsInstance(resp['raw']['password'], str)
        self.assertIsInstance(resp['raw']['port'], int)
        self.assertIsInstance(resp['raw']['sslmode'], str)
        self.assertIsInstance(resp['raw']['user'], str)
        self.assertIsInstance(resp['connectionStrings'], dict)
        self.assertEqual(len(resp['connectionStrings']), 5)
        self.assertTrue(resp['connectionStrings']['jdbc'].startswith('jdbc:postgresql://'))
        self.assertTrue(resp['connectionStrings']['libpq'].startswith('host='))
        self.assertTrue(resp['connectionStrings']['net'].startswith('Server='))
        self.assertTrue(resp['connectionStrings']['psql'].startswith('psql \'host='))
        self.assertTrue(resp['connectionStrings']['url'].startswith('postgresql://'))

    def test_storage(self) -> None:
        '''perform storage device info on every device from storage device list'''

        devices = self.API.account_storage_devices()
        self.assertEqual(devices['result'], 'success')
        with self.subTest():
            for device in devices['storages']:
                d: Dict[str, Any] = self.API.storage(device['name'])
                self.assertEqual(d['result'], 'success')
                if d['type'] == 'azure_afs':
                    self.assertEqual(len(d), 12)
                    self.storage_azure_afs(d)
                if d['type'] == 'azure_workspace':
                    self.assertEqual(len(d), 17)
                    self.storage_azure_workspace(d)
                elif d['type'] == 'onedrive':
                    self.assertEqual(len(d), 24)
                    self.storage_onedrive(d)
                    # connect is not in get devices call due to real time performance
                    self.assertIsInstance(d['connected'], bool)
                elif d['type'] == 'postgres_db':
                    # storage item contains an additional result key
                    self.assertEqual(len(d), 23)
                    self.storage_database(d)

    def test_storage_attr(self) -> None:
        '''device attributes: annotations, label, and tag'''

        attrs: Tuple[Literal['annotation'], Literal['label'], Literal['tag']] = (
            'annotation',
            'label',
            'tag',
        )
        devices: Dict[str, Any] = self.API.account_storage_devices()
        self.assertEqual(devices['result'], 'success')
        with self.subTest():
            for d in devices['storages']:
                for a in attrs:
                    resp: Dict[str, Any] = self.API._storage_attr(d['name'], a)
                    self.assertEqual(resp['result'], 'success')
                    self.assertEqual(len(resp.keys()), 2)
                    a += 's'  #  BUG PR-924 route vs attribute is not the same
                    self.assertTrue(a in resp.keys())
                    if a == 'tags':
                        self.assertIsInstance(resp[a], str)
                    else:
                        self.assertIsInstance(resp[a], dict)

    @unittest.skip('api has not implemented')
    def test_storage_disk_create(self):
        '''create a new file storage device'''

        raise NotImplementedError

    @unittest.skip('api is incomplete')
    def test_storage_delete(self):
        '''delete storage device'''

        raise NotImplementedError

    def test_sql_query(self) -> None:
        '''test sql statement execution'''

        self.database_ensure_exist()
        pg = self.API.account_storage_device(type='postgres_db')
        resp = self.API.sql_query(
            database_name=pg['name'], query='SELECT datname FROM pg_database;'
        )
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['rowCount'], int)
        self.assertGreaterEqual(resp['rowCount'], 1)
        self.assertIsInstance(resp['queryResults'], list)
        self.assertGreaterEqual(len(resp['queryResults']), 1)

    def test_util_env(self) -> None:
        '''atlas and andromeda common environment variables'''

        keys: Tuple[str, ...] = (
            'job_cmd',
            'job_dir',
            'job_key',
            'job_api',
            'job_img',
            'pip_ver',
            'py_ver',
        )
        d = self.API.util_environment()
        for k in d.keys():
            self.assertTrue(k in keys)
            self.assertIsInstance(d[k], str)

    def test_util_job_monitor_bad(self) -> None:
        '''job monitor check invalid job key or job state'''

        # invalid job state
        with self.assertRaises(ValueError):
            self.API.util_job_monitor(self.WKSP, '5633e372-337a-454c-aae4-10084ea5bac6', 'invalid')  # type: ignore
        # invalid job key
        with self.assertRaises(ValueError):
            self.API.util_job_monitor(self.WKSP, '')
        with self.assertRaises(ValueError):
            self.API.util_job_monitor(self.WKSP, 'invalid')
        with self.assertRaises(ValueError):
            self.API.util_job_monitor(self.WKSP, '633e372-337a-454c-aae4-10084ea5bac6')
        # valid but job key does not exist
        resp: bool = self.API.util_job_monitor(self.WKSP, '00000000-0000-0000-0000-000000000000')
        self.assertFalse(resp)

    def test_wksp_file_copy(self) -> None:
        '''make a copy of a file within a workspace'''

        src: str = self.py_run_me
        dest: str = f'{self.dir_testdata_remote}/cp_test.txt'
        resp = self.API.wksp_file_copy(
            self.WKSP, file_path_src=src, file_path_dest=dest, overwrite=True
        )
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['copyStatus'], 'success')
        self.assertEqual(resp['message'], 'Copy complete')
        src_result: str = (
            f"{resp['sourceFileInfo']['directoryPath']}/{resp['sourceFileInfo']['filename']}"
        )
        dest_result: str = (
            f"{resp['targetFileInfo']['directoryPath']}/{resp['targetFileInfo']['filename']}"
        )
        self.assertEqual(src, src_result)
        self.assertEqual(dest, dest_result)

    def test_wksp_file_delete(self) -> None:
        '''delete a copied file with a workspace'''

        f: str = f'{self.dir_testdata_remote}/cp_test.txt'
        resp = self.API.wksp_file_delete(self.WKSP, file_path=f)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['message'], 'File deleted')
        file_result = f"{resp['fileInfo']['directoryPath']}/{resp['fileInfo']['filename']}"
        self.assertEqual(f, file_result)

    def test_wksp_file_download(self) -> None:
        '''download a file from a given workspace'''

        download = self.API.wksp_file_download(self.WKSP, file_path=self.py_run_me)
        self.assertGreaterEqual(len(download), 1)
        self.assertIsInstance(download, str)

    def test_wksp_file_download_crash(self) -> None:
        '''download a file from a given workspace'''

        resp: str = self.API.wksp_file_download(self.WKSP, file_path='does_not_exist')
        self.assertIsInstance(resp, str)
        r: dict = loads(resp)
        self.assertEqual(r['result'], 'error')
        self.assertIsInstance(r['error'], str)
        self.assertEqual(len(r['correlationId']), 36)

    def test_wksp_file_download_meta(self) -> None:
        '''file metadata'''

        resp = self.API.wksp_file_download_status(self.WKSP, file_path=self.py_run_me)
        self.assertEqual(resp['result'], 'success')
        keys: Tuple[str, ...] = (
            'result',
            'workspace',
            'filename',
            'directoryPath',
            'filePath',
            'lastModified',
            'contentLength',
            'date',
            'fileCreatedOn',
            'fileLastWriteOn',
            'fileChangeOn',
        )
        for key in resp.keys():
            self.assertIn(key, keys)
        self.assertEqual(resp['filePath'], self.py_run_me)
        self.assertEqual(resp['workspace'], self.WKSP)
        self.assertIsInstance(resp['contentLength'], int)
        dt: datetime = parse(resp['lastModified'])
        self.assertEqual(dt.tzname(), 'UTC')

    def test_wksp_file_upload(self) -> None:
        '''upload a file to a workspace'''

        dest: str = f'{self.dir_testdata_remote}/str2file.txt'
        resp = self.API.wksp_file_upload(
            self.WKSP, file_path_dest=dest, overwrite=True, filestr='test'
        )
        self.assertEqual(resp['result'], 'success')
        self.assertIn(resp['message'], ['File created', 'File replaced'])

    def test_wksp_files(self) -> None:
        '''file structure from a given workspace and must have at least one file'''

        resp = self.API.wksp_files(self.WKSP)
        self.assertEqual(resp['result'], 'success')
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['files'], list)
        self.assertGreaterEqual(len(resp['files']), 1)
        self.assertTrue(resp['files'][0].get('filename'))
        self.assertTrue(resp['files'][0].get('directoryPath'))
        self.assertTrue(resp['files'][0].get('filePath'))
        self.assertTrue(resp['files'][0].get('contentLength'))

    def test_wksp_folder_delete(self) -> None:
        '''delete a folder from a workspace'''

        folder: str = 'delmenow'
        fp: str = os.path.join(folder, 'delme.txt')
        self.API.wksp_file_upload(self.WKSP, fp, filestr='first file line')
        resp = self.API.wksp_folder_delete(self.WKSP, dir_path=folder, force=True)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['message'], 'Directory and all contents deleted')
        self.assertEqual(resp['directoryPath'], folder)

    def test_wksp_info(self) -> None:
        '''properties of a given workspace'''

        resp = self.API.wksp_info(self.WKSP)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['name'], self.WKSP)
        self.assertEqual(len(resp['key']), 25)
        self.assertRegex(resp['key'], '^workspace')
        self.assertIn(resp['stack'], ['Optilogic', 'Simulation', 'Gurobi'])
        self.assertTrue(resp['status'].isupper())

    def test_wksp_job_back2back(self) -> None:
        '''one job to run many python modules in a row'''

        item_one: dict = {
            'pyModulePath': '/projects/quick_tests/sleep.py',
            'commandArgs': 'not_used',
            'timeout': 90,
        }
        item_two: dict = {
            'pyModulePath': '/projects/quick_tests/airline_hub_location_cbc.py',
            'timeout': 30,
        }
        batch = {'batchItems': [item_one, item_two]}

        tag: str = 'unittest_batch_back2back'
        resp = self.API.wksp_job_back2back(self.WKSP, batch=batch, verboseOutput=True, tags=tag)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp), 5)
        self.assertEqual(resp['message'], 'Job submitted')
        self.assertIsInstance(resp['jobKey'], str)
        self.assertEqual(len(resp['jobKey']), 36)
        self.assertIsInstance(resp['batch'], dict)
        self.assertEqual(len(resp['batch']), 1)

        # batchItems
        self.assertIsInstance(batch['batchItems'], list)
        self.assertEqual(len(batch['batchItems']), 2)
        # item_one
        self.assertIsInstance(resp['batch']['batchItems'][0], list)
        self.assertEqual(len(resp['batch']['batchItems'][0]), 3)
        self.assertEqual(resp['batch']['batchItems'][0][0], item_one['pyModulePath'])
        self.assertEqual(resp['batch']['batchItems'][0][1], item_one['commandArgs'])
        self.assertEqual(resp['batch']['batchItems'][0][2], item_one['timeout'])
        # item_two
        self.assertIsInstance(resp['batch']['batchItems'][1], list)
        self.assertEqual(len(resp['batch']['batchItems'][1]), 3)
        self.assertEqual(resp['batch']['batchItems'][1][0], item_two['pyModulePath'])
        self.assertIsNone(resp['batch']['batchItems'][1][1])
        self.assertEqual(resp['batch']['batchItems'][1][2], item_two['timeout'])

        # jobInfo
        self.assertIsInstance(resp['jobInfo'], dict)
        self.assertEqual(len(resp['jobInfo']), 4)
        self.assertEqual(resp['jobInfo']['workspace'], self.WKSP)
        self.assertEqual(resp['jobInfo']['tags'], tag)
        self.assertEqual(resp['jobInfo']['timeout'], -1)
        self.assertIsInstance(resp['jobInfo']['resourceConfig'], dict)
        self.assertEqual(len(resp['jobInfo']['resourceConfig']), 4)
        self.assertEqual(resp['jobInfo']['resourceConfig']['cpu'], '1vCore')
        self.assertEqual(resp['jobInfo']['resourceConfig']['name'], '3XS')
        self.assertEqual(resp['jobInfo']['resourceConfig']['ram'], '2Gb')
        self.assertEqual(resp['jobInfo']['resourceConfig']['run_rate'], 2)

        # verify new batch job
        job = self.API.wksp_job_status(self.WKSP, resp['jobKey'])
        self.assertEqual(job['jobInfo']['workspace'], self.WKSP)
        self.assertEqual(job['jobInfo']['directoryPath'], '/usr/bin')
        self.assertEqual(job['jobInfo']['filename'], 'batch_run.py')
        self.assertEqual(job['jobInfo']['command'], 'run')
        self.assertIsInstance(job['jobInfo']['commandArgs'], str)
        args: dict = loads(job['jobInfo']['commandArgs'][1:-1])
        self.assertIsInstance(args, dict)
        self.assertIsInstance(args['batchItems'], list)
        self.assertEqual(args['batchItems'][0][0], item_one['pyModulePath'])
        self.assertEqual(args['batchItems'][0][1], item_one['commandArgs'])
        self.assertEqual(args['batchItems'][0][2], item_one['timeout'])
        self.assertEqual(args['batchItems'][1][0], item_two['pyModulePath'])
        self.assertEqual(args['batchItems'][1][1], item_two.get('commandArgs'))
        self.assertEqual(args['batchItems'][1][2], item_two['timeout'])
        self.assertEqual(job['jobInfo']['resourceConfig']['cpu'], '1vCore')
        self.assertEqual(job['jobInfo']['resourceConfig']['name'], '3XS')
        self.assertEqual(job['jobInfo']['resourceConfig']['ram'], '2Gb')
        self.assertEqual(job['jobInfo']['resourceConfig']['run_rate'], 2)

    def test_wksp_job_back2back_findnrun(self) -> None:
        '''search file paths yields one job to run many python modules in a row'''

        item_one: dict = {
            'pySearchTerm': '/projects/quick_tests/sleep.py',
            'commandArgs': 'not_used',
            'timeout': 90,
        }
        item_two: dict = {
            'pySearchTerm': '/projects/quick_tests/airline_hub_location_cbc.py',
            'timeout': 30,
        }
        batch = {'batchItems': [item_one, item_two]}

        tag: str = 'unittest_batch_back2back_find'
        resp = self.API.wksp_job_back2back_findnrun(
            self.WKSP, batch=batch, verboseOutput=True, tags=tag
        )
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp), 5)
        self.assertEqual(resp['message'], 'Job submitted')
        self.assertIsInstance(resp['jobKey'], str)
        self.assertEqual(len(resp['jobKey']), 36)
        self.assertIsInstance(resp['batch'], dict)
        self.assertEqual(len(resp['batch']), 2)
        self.assertTrue(resp['batch']['search'])

        # batchItems
        self.assertIsInstance(batch['batchItems'], list)
        self.assertEqual(len(batch['batchItems']), 2)
        # item_one
        self.assertIsInstance(resp['batch']['batchItems'][0], list)
        self.assertEqual(len(resp['batch']['batchItems'][0]), 3)
        self.assertEqual(resp['batch']['batchItems'][0][0], item_one['pySearchTerm'])
        self.assertEqual(resp['batch']['batchItems'][0][1], item_one['commandArgs'])
        self.assertEqual(resp['batch']['batchItems'][0][2], item_one['timeout'])
        # item_two
        self.assertIsInstance(resp['batch']['batchItems'][1], list)
        self.assertEqual(len(resp['batch']['batchItems'][1]), 3)
        self.assertEqual(resp['batch']['batchItems'][1][0], item_two['pySearchTerm'])
        self.assertIsNone(resp['batch']['batchItems'][1][1])
        self.assertEqual(resp['batch']['batchItems'][1][2], item_two['timeout'])

        # jobInfo
        self.assertIsInstance(resp['jobInfo'], dict)
        self.assertEqual(len(resp['jobInfo']), 4)
        self.assertEqual(resp['jobInfo']['workspace'], self.WKSP)
        self.assertEqual(resp['jobInfo']['tags'], tag)
        self.assertEqual(resp['jobInfo']['timeout'], -1)
        self.assertIsInstance(resp['jobInfo']['resourceConfig'], dict)
        self.assertEqual(len(resp['jobInfo']['resourceConfig']), 4)
        self.assertEqual(resp['jobInfo']['resourceConfig']['cpu'], '1vCore')
        self.assertEqual(resp['jobInfo']['resourceConfig']['name'], '3XS')
        self.assertEqual(resp['jobInfo']['resourceConfig']['ram'], '2Gb')
        self.assertEqual(resp['jobInfo']['resourceConfig']['run_rate'], 2)

        # verify new batch job
        job = self.API.wksp_job_status(self.WKSP, resp['jobKey'])
        self.assertEqual(job['jobInfo']['workspace'], self.WKSP)
        self.assertEqual(job['jobInfo']['directoryPath'], '/usr/bin')
        self.assertEqual(job['jobInfo']['filename'], 'batch_search_n_run.py')
        self.assertEqual(job['jobInfo']['command'], 'run')
        self.assertIsInstance(job['jobInfo']['commandArgs'], str)
        args: dict = loads(job['jobInfo']['commandArgs'][1:-1])
        self.assertIsInstance(args, dict)
        self.assertIsInstance(args['batchItems'], list)
        self.assertEqual(args['batchItems'][0][0], item_one['pySearchTerm'])
        self.assertEqual(args['batchItems'][0][1], item_one['commandArgs'])
        self.assertEqual(args['batchItems'][0][2], item_one['timeout'])
        self.assertEqual(args['batchItems'][1][0], item_two['pySearchTerm'])
        self.assertEqual(args['batchItems'][1][1], item_two.get('commandArgs'))
        self.assertEqual(args['batchItems'][1][2], item_two['timeout'])
        self.assertEqual(job['jobInfo']['resourceConfig']['cpu'], '1vCore')
        self.assertEqual(job['jobInfo']['resourceConfig']['name'], '3XS')
        self.assertEqual(job['jobInfo']['resourceConfig']['ram'], '2Gb')
        self.assertEqual(job['jobInfo']['resourceConfig']['run_rate'], 2)

    def test_wksp_job_file_error(self) -> None:
        '''get job error file'''

        resp: str = self.API.wksp_job_file_error(self.WKSP, self.API._job_start_recent_key)
        self.assertIsInstance(resp, str)
        if resp.startswith('{\"result\":\"error\"'):
            err: dict = loads(resp)
            self.assertEqual(err['result'], 'error')
            self.assertIsInstance(err['error'], str)
            self.assertIsInstance(err['correlationId'], str)
            self.assertEqual(len(err['correlationId']), 36)
        else:
            self.assertGreater(len(resp), 0)

    def test_wksp_job_file_result(self) -> None:
        '''get job result file'''

        resp: str = self.API.wksp_job_file_result(self.WKSP, self.API._job_start_recent_key)
        self.assertIsInstance(resp, str)
        if resp.startswith('{\"result\":\"error\"'):
            err: dict = loads(resp)
            self.assertEqual(err['result'], 'error')
            self.assertIsInstance(err['error'], str)
            self.assertIsInstance(err['correlationId'], str)
            self.assertEqual(len(err['correlationId']), 36)
        else:
            self.assertGreater(len(resp), 0)

    def test_wksp_job_ledger(self) -> None:
        '''get job ledger that has realtime messages'''

        if len(self.__jobkey_quick) == 0:
            self.job_prereq()
        resp = self.API.wksp_job_ledger(self.WKSP, self.__jobkey_quick)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['records'], list)
        self.assertGreaterEqual(len(resp['records']), 1)
        self.assertIsInstance(resp['records'][0]['timestamp'], int)
        self.assertIsInstance(resp['records'][0]['datetime'], str)
        # job was created during init, assert same day
        self.assertTrue(resp['records'][0]['datetime'].endswith('Z'))
        dt: datetime = parse(resp['records'][0]['datetime'])
        self.assertTrue(dt.tzname(), 'UTC')
        now: datetime = datetime.utcnow()
        self.assertEqual(dt.year, now.year)
        self.assertEqual(dt.month, now.month)
        self.assertEqual(dt.day, now.day)

    def test_wksp_job_metrics(self) -> None:
        '''get one second cpu and memory sampling of a job'''

        if len(self.__jobkey_quick) == 0:
            self.job_prereq()
        resp = self.API.wksp_job_metrics(self.WKSP, self.__jobkey_quick)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertGreaterEqual(resp['count'], 1)
        self.assertIsInstance(resp['max'], dict)
        self.assertEqual(len(resp['max']), 7)
        self.assertIsInstance(resp['max']['memoryPercent'], float)
        self.assertIsInstance(resp['max']['memoryResident'], Number)
        self.assertIsInstance(resp['max']['memoryAvailable'], int)
        self.assertIsInstance(resp['max']['cpuPercent'], float)
        self.assertIsInstance(resp['max']['cpuUsed'], float)
        self.assertIsInstance(resp['max']['cpuAvailable'], Number)
        self.assertIsInstance(resp['max']['processCount'], int)
        self.assertIsInstance(resp['records'], list)
        self.assertGreaterEqual(len(resp['records']), 1)
        self.assertIsInstance(resp['records'][0]['timestamp'], int)
        self.assertIsInstance(resp['records'][0]['datetime'], str)
        self.assertTrue(resp['records'][0]['datetime'].endswith('Z'))
        dt: datetime = parse(resp['records'][0]['datetime'])
        self.assertTrue(dt.tzname(), 'UTC')
        now: datetime = datetime.utcnow()
        self.assertEqual(dt.year, now.year)
        self.assertEqual(dt.month, now.month)
        self.assertEqual(dt.day, now.day)
        self.assertIsInstance(resp['records'][0], dict)
        self.assertIsInstance(resp['records'][0]['cpuAvailable'], Number)
        self.assertIsInstance(resp['records'][0]['cpuPercent'], float)
        self.assertIsInstance(resp['records'][0]['cpuUsed'], float)
        self.assertIsInstance(resp['records'][0]['memoryAvailable'], int)
        self.assertIsInstance(resp['records'][0]['memoryPercent'], float)
        self.assertIsInstance(resp['records'][0]['memoryResident'], float)
        self.assertIsInstance(resp['records'][0]['processCount'], int)

    def test_wksp_job_metrics_max(self) -> None:
        '''get peak cpu and memory stats of a job'''

        if len(self.__jobkey_quick) == 0:
            self.job_prereq()
        resp = self.API.wksp_job_metrics_max(self.WKSP, self.__jobkey_quick)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['max'], dict)
        self.assertEqual(len(resp['max']), 7)
        self.assertIsInstance(resp['max']['memoryPercent'], float)
        self.assertIsInstance(resp['max']['memoryResident'], float)
        self.assertIsInstance(resp['max']['memoryAvailable'], int)
        self.assertIsInstance(resp['max']['cpuPercent'], float)
        self.assertIsInstance(resp['max']['cpuUsed'], Number)
        self.assertIsInstance(resp['max']['cpuAvailable'], Number)
        self.assertIsInstance(resp['max']['processCount'], int)

    def test_wksp_job_metrics_mia(self) -> None:
        '''
        OE-5276 Job Metrics are Missing Sometimes
        OE-5369 Job Metrics Missing v3
        '''

        # spin up a few jobs to create load and evaluate all
        jobs_max: int = 9
        tag_time: float = time.time()
        tag: str = f'metrics_{tag_time}'
        secs: int = 20
        d: dict = {}  # store job key and elapsed time without metrics
        for job in range(jobs_max):
            resp = self.API.wksp_job_start(
                self.WKSP, self.py_run_me, tags=tag, timeout=secs, resourceConfig='mini'
            )
            if resp.get('crash'):
                print(resp)
                jobs_max -= 1
                continue  
            d[resp['jobKey']] = {'seen_first': None, 'missing_last': None}

        # check the jobs that are about to run
        metrics_missing = False
        check: bool = True
        while check:
            # stop if all jobs finished
            jobs: Dict[str, Any] = self.API.wksp_jobs(self.WKSP, tags=tag)
            terminal: int = 0
            for t in self.API.JOBSTATES_TERMINAL:
                terminal += jobs['statusCounts'].get(t)
            if terminal == jobs_max:
                check = False
                break

            # check running jobs for metrics
            active: Dict[str, Any] = self.API.wksp_jobs(self.WKSP, status='running', tags=tag)
            for job in active['jobs']:
                # elapsed run time
                st: str = str(job['startDatetime'])
                st = st.replace('T', ' ')
                st = st.replace('Z', '')
                job_start: datetime = datetime.fromisoformat(st)
                now: datetime = datetime.utcnow()
                delta: timedelta = now - job_start

                # first time observed the job was running
                if d[job['jobKey']].get('seen_first') is None:
                    d[job['jobKey']]['seen_first'] = str(delta)

                # check for metrics
                resp: Dict[str, Any] = self.API.wksp_job_metrics(self.WKSP, job['jobKey'])
                self.assertEqual(resp['result'], 'success')
                self.assertIsInstance(resp['count'], int)

                # missing metrics?
                if resp['count'] == 0:
                    metrics_missing = True
                    d[job['jobKey']]['missing_last'] = str(delta)
                    print(f"{str(delta)} secs elapsed, metrics missing for job {job['jobKey']}")
                    with self.subTest():
                        self.assertLess(delta.total_seconds(), 10)

        if metrics_missing:
            print('\n\nTEST_WKSP_JOB_METRICS_MIA')
            print(f"\n\nJob Submitted: {jobs_max}, Job Duration: {secs}, Job Tag: {tag}")
            for item in d.items():
                print(item)

    def test_wksp_job_start(self) -> None:
        '''creating a job'''

        resp = self.API.wksp_job_start(
            self.WKSP, file_path=self.py_run_me, tags='unittest_start', resourceConfig='mini'
        )
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp['jobKey']), 36)
        job_info_keys: Tuple[str, ...] = (
            'workspace',
            'directoryPath',
            'filename',
            'command',
            'resourceConfig',
            'tags',
            'timeout',
        )
        for key in resp['jobInfo'].keys():
            self.assertIn(key, job_info_keys)

    def test_wksp_job_start_preview(self) -> None:
        '''create a job using andromeda preview image and compare to stable'''

        job_beta: Dict[str, Any] = self.API.wksp_job_start(
            self.WKSP,
            file_path=self.py_run_me_bash,
            commandArgs="'pip list -v'",
            resourceConfig='mini',
            tags='unittest',
            preview_image=True,
        )
        self.assertEqual(job_beta['result'], 'success')

        job: Dict[str, Any] = self.API.wksp_job_start(
            self.WKSP,
            file_path=self.py_run_me_bash,
            commandArgs="'pip list -v'",
            resourceConfig='mini',
            tags='unittest',
            preview_image=False,
        )
        self.assertEqual(job['result'], 'success')

        done = self.API.util_job_monitor(self.WKSP, job_key=job_beta['jobKey'], stop_when='done')
        self.assertTrue(done)
        std_out: str = self.API.wksp_job_file_result(self.WKSP, job_beta['jobKey'])
        self.assertIsInstance(std_out, str)
        self.assertGreater(len(std_out), 100)
        m = search(r'(?P<pkg>neo)\s+(?P<ver>[\w\.]+)', std_out)
        version_preview: str = m.groupdict()['ver'] if m else ''
        self.assertRegex(version_preview, r'2\.[6-9]\.\d+')

        done = self.API.util_job_monitor(self.WKSP, job_key=job['jobKey'], stop_when='done')
        self.assertTrue(done)
        std_out: str = self.API.wksp_job_file_result(self.WKSP, job['jobKey'])
        self.assertIsInstance(std_out, str)
        self.assertGreater(len(std_out), 100)
        m = search(r'(?P<pkg>neo)\s+(?P<ver>[\w\.]+)', std_out)
        version: str = m.groupdict()['ver'] if m else ''
        self.assertRegex(version, r'2\.5\.\d+')

        self.assertNotEqual(version, version_preview)

    def test_wksp_job_start_sample(self) -> None:
        '''create job api call reponse time is the slowest and fails often withg 504s'''

        max: int = int(self.API.account_info()['limits']['concurrentJobs'] * 0.5)
        min: int = 10
        job_count: int = max if max > min else min
        jobs: List[str] = []
        tag: str = 'unittest_job_speed'

        # start jobs
        for j in range(job_count):
            with self.subTest():
                resp = self.API.wksp_job_start(
                    self.WKSP, self.py_run_me_quick, tags=tag, resourceConfig='mini'
                )
                self.assertEqual(resp['result'], 'success')
            # d = {}
            # d['key'] = resp['jobKey']
            # jobs.append(d)
            # spin up a few jobs to create load and evaluate all

        return
        # what is current job count
        jobs_active: int = self.API._jobs_active
        jobs_max: int = self.API.account_info()['limits']['concurrentJobs']
        max: int = jobs_max - jobs_active if jobs_max > jobs_active else 0

        jobs_max: int = 9
        tag_time: float = time.time()
        tag: str = f'unittest_job_sample_{tag_time}'

        for job in range(jobs_max):
            self.API.wksp_job_start(self.WKSP, self.py_run_me, tags=tag)

        # check the jobs that are about to run
        d: dict = {}
        check: bool = True
        while check:
            jobs = self.API.wksp_jobs(self.WKSP, tags=tag)

            # jobs all finished?
            terminal: int = 0
            for t in self.API.JOBSTATES_TERMINAL:
                terminal += jobs['statusCounts'].get(t)

            if terminal == jobs_max:
                check = False
                break

            # check running jobs for metrics
            active = self.API.wksp_jobs(self.WKSP, status='running', tags=tag)

            if active['statusCounts']['running'] >= 1:
                for job in active['jobs']:
                    resp = self.API.wksp_job_metrics(self.WKSP, job['jobKey'])
                    self.assertEqual(resp['result'], 'success')
                    self.assertIsInstance(resp['count'], int)
                    # self.assertGreaterEqual(resp['count'], 1)

                    # missing metrics!
                    if resp['count'] == 0:
                        st: str = str(job['startDatetime'])
                        st = st.replace('T', ' ')
                        st = st.replace('Z', '')
                        job_start: datetime = datetime.fromisoformat(st)
                        now: datetime = datetime.utcnow()
                        delta: timedelta = now - job_start
                        d[job['jobKey']] = str(
                            delta
                        )  # store job key and elapsed time without metrics

                        print(
                            f"{str(delta)} secs elapsed and metrics missing for job {job['jobKey']}"
                        )
                        with self.subTest():
                            self.assertLess(delta.total_seconds(), 5)

            time.sleep(1)

        # were there any jobs that failed metric check?
        secs = 0
        if len(d) >= 1:
            print(f"\n\nJob Submitted: {jobs_max}, Job Duration: {secs}, Job Tag: {tag}")
            print('\n JobKey, LastSeenWithMissingMetricCount_RunDuration')
            for k in d.items():
                print(k[1], k[0])

    def test_wksp_job_status(self) -> None:
        '''get job status for explicit state'''

        resp = self.API.wksp_job_status(self.WKSP, self.API._job_start_recent_key)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp['jobKey']), 36)
        self.assertIsInstance(resp['submittedDatetime'], str)
        self.assertTrue(resp['submittedDatetime'].endswith('Z'))
        dt: datetime = parse(resp['submittedDatetime'])
        self.assertTrue(dt.tzname(), 'UTC')
        now: datetime = datetime.utcnow()
        self.assertEqual(dt.year, now.year)
        self.assertEqual(dt.month, now.month)
        self.assertEqual(dt.day, now.day)
        self.assertIn(resp['status'], self.API.JOBSTATES)
        job_info_keys: Tuple[str, ...] = (
            'workspace',
            'directoryPath',
            'filename',
            'command',
            'errorFile',
            'resultFile',
            'resourceConfig',
            'tags',
            'timeout',
        )
        for key in resp['jobInfo'].keys():
            self.assertIn(key, job_info_keys)
        self.assertEqual(resp['jobInfo']['command'], 'run')
        self.assertIsInstance(resp['jobInfo']['errorFile'], bool)
        self.assertIsInstance(resp['jobInfo']['resultFile'], bool)
        resource_keys: Tuple[str, ...] = ('name', 'cpu', 'ram', 'run_rate')
        for key in resp['jobInfo']['resourceConfig']:
            self.assertIn(key, resource_keys)

    def test_wksp_job_stop(self) -> None:
        '''stop a most recently created job'''

        # guarantee a job is currently running
        resp = self.API.wksp_job_status(self.WKSP, self.API._job_start_recent_key)
        if resp['status'] in self.API.JOBSTATES_TERMINAL:
            resp = self.API.wksp_job_start(self.WKSP, self.py_run_me, resourceConfig='mini')
            success: bool = self.API.util_job_monitor(self.WKSP, resp['jobKey'])
            if success is False:
                self.skipTest('failed to start job within two minutes')

        # stop running job
        resp = self.API.wksp_job_stop(self.WKSP, self.API._job_start_recent_key)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['jobKey'], self.API._job_start_recent_key)
        keys: Tuple[str, ...] = ('result', 'message', 'jobKey', 'status', 'jobInfo')
        for key in resp.keys():
            self.assertIn(key, keys)

    def test_wksp_jobify(self) -> None:
        '''batch queue many jobs'''

        batch = {
            'batchItems': [
                {'pyModulePath': '/projects/quick_tests/sleep.py', 'timeout': 90},
                {
                    'pyModulePath': '/projects/quick_tests/airline_hub_location_cbc.py',
                    'timeout': 30,
                },
            ]
        }

        tag: str = 'unittest_batch_jobify'
        resp = self.API.wksp_jobify(self.WKSP, batch=batch, tags=tag)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['message'], 'Jobs submitted')
        self.assertIsInstance(resp['count'], int)
        self.assertEqual(resp['count'], len(resp['jobKeys']))
        for key in resp['jobKeys']:
            self.assertIsInstance(key, str)
            self.assertEqual(len(key), 36)

    def test_wksp_jobify_findnrun(self) -> None:
        '''search file paths yields many jobs to run each python module found'''

        batch = {
            'batchItems': [
                {'pySearchTerm': '^/quick_tests/sleep.py', 'timeout': 90},
                {'pySearchTerm': '^/quick_tests/airline_hub_location_cbc.py', 'timeout': 30},
            ]
        }

        tag: str = 'unittest_batch_jobify_find'
        resp = self.API.wksp_jobify_findnrun(self.WKSP, batch=batch, tags=tag)
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['message'], 'Jobs submitted')
        self.assertIsInstance(resp['count'], int)
        self.assertEqual(len(batch['batchItems']), resp['count'])
        self.assertEqual(resp['count'], len(resp['jobKeys']))
        for key in resp['jobKeys']:
            self.assertIsInstance(key, str)
            self.assertEqual(len(key), 36)

    def test_wksp_jobs(self) -> None:
        '''list the jobs for a specific workspace'''

        resp = self.API.wksp_jobs(self.WKSP)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertIsInstance(resp['statusCounts'], dict)

        status_keys: Tuple[str, ...] = self.API.JOBSTATES
        for status in resp['statusCounts']:
            self.assertIn(status, status_keys)
            self.assertGreaterEqual(resp['statusCounts'][status], 0)

        self.assertIsInstance(resp['tagCounts'], dict)
        self.assertIsInstance(resp['filters'], dict)

        filter_keys: Tuple[str, ...] = (
            'command',
            'history',
            'runSecsMax',
            'runSecsMin',
            'status',
            'tags',
        )
        for filter in resp['filters']:
            self.assertIn(filter, filter_keys)

        self.assertGreaterEqual(len(resp['jobs']), 1)
        job_keys: Tuple[str, ...] = (
            'jobKey',
            'submittedDatetime',
            'startDatetime',
            'endDatetime',
            'runTime',
            'runRate',
            'billedTime',
            'status',
            'jobInfo',
            'waitTime',
        )
        for job in resp['jobs']:
            for key, value in job.items():
                self.assertIn(key, job_keys)
                if key.lower().find('datetime') > -1 and value:
                    with self.subTest():
                        dt: datetime = parse(value)
                        self.assertEqual(dt.tzname(), 'UTC')
                if key == 'jobInfo':
                    if job[key]['command'] == 'run':
                        self.assertIsInstance(job[key]['directoryPath'], str)
                        self.assertIsInstance(job[key]['filename'], str)
                    self.assertIsInstance(job[key]['resourceConfig'], dict)
                    self.assertIsInstance(job[key]['workspace'], str)

    def test_wksp_jobs_stats(self) -> None:
        '''get the stats for jobs for a specific workspace'''

        resp = self.API.wksp_jobs(self.WKSP)
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['count'], int)
        self.assertIsInstance(resp['statusCounts'], dict)

        status_keys: Tuple[str, ...] = self.API.JOBSTATES
        for status in resp['statusCounts']:
            self.assertIn(status, status_keys)
            self.assertGreaterEqual(resp['statusCounts'][status], 0)

        self.assertIsInstance(resp['tagCounts'], dict)
        self.assertIsInstance(resp['filters'], dict)

        filter_keys: Tuple[str, ...] = (
            'command',
            'history',
            'runSecsMax',
            'runSecsMin',
            'status',
            'tags',
        )
        for filter in resp['filters']:
            self.assertIn(filter, filter_keys)

    def test_wksp_share_file(self) -> None:
        '''share a file from a workspace to all other workspaces of a user/self'''

        if self.API.auth_username is None:
            self.skipTest('test_wksp_share_folder requires a username')

        resp = self.API.wksp_share_file(
            self.WKSP, file_path=self.py_run_me, targetUsers=self.API.auth_username
        )
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp.keys()), 8)
        self.assertIsInstance(resp['errored'], list)
        self.assertEqual(len(resp['errored']), 0)
        self.assertIsInstance(resp['erroredCount'], int)
        self.assertIsInstance(resp['jobs'], list)
        self.assertEqual(len(resp['jobs']), self.API.account_workspace_count - 1)
        for j in resp['jobs']:
            self.assertIsInstance(j['jobKey'], str)
            self.assertIsInstance(j['result'], str)
            self.assertEqual(j['result'], 'success')
        self.assertEqual(resp['jobsCount'], self.API.account_workspace_count - 1)
        self.assertIsInstance(resp['message'], str)
        self.assertEqual(resp['message'], 'Share Accepted')
        self.assertIsInstance(resp['sourceFileInfo'], dict)
        self.assertEqual(len(resp['sourceFileInfo'].keys()), 2)
        self.assertIsInstance(resp['sourceFileInfo']['directoryPath'], str)
        self.assertEqual(resp['sourceFileInfo']['directoryPath'], os.path.split(self.py_run_me)[0])
        self.assertIsInstance(resp['sourceFileInfo']['filename'], str)
        self.assertEqual(resp['sourceFileInfo']['filename'], os.path.split(self.py_run_me)[1])
        self.assertEqual(resp['targetUsers'], self.API.auth_username)

    def test_wksp_share_file_sample(self) -> None:
        '''OE-5840 API Share File/Folder Results in 500 Internal Server Error'''

        if self.API.auth_username is None:
            self.skipTest('test_wksp_share_folder requires a username')

        if self.API.account_workspace_count < 2:
            self.skipTest('account does not have required multi-workspaces needed for sharing')

        test_result: bool = False

        # get all not Studio workspaces
        resp: dict = self.API.account_workspaces()
        wksp_names: list[str] = [w['name'] for w in resp['workspaces'] if w['name'] != 'Studio']
        wksp_not_studio: str = wksp_names[0]

        # upload files to share
        filenames: list[str] = []
        filepaths: list[str] = []
        tag: int = time.perf_counter_ns()
        for x in range(10):
            filename: str = f'{tag}_{x}.txt'
            file_path: str = f'/My Files/{tag}/{filename}'
            file_contents: str = f'{datetime.now()} {tag}_{x} unittest test_wksp_share_file_sample'
            resp = self.API.wksp_file_upload('Studio', file_path, filestr=file_contents)
            if resp.get('crash'):
                print(f'{x} {filename} upload attempt failed')
                continue
            filenames.append(filename)
            filepaths.append(file_path)

        # verify uploaded files arrived
        up_arrived: bool = False
        up_count_verified: int = 0
        up_start: float = time.perf_counter()
        while up_arrived is False and time.perf_counter() - up_start < 30:
            resp = self.API.wksp_files('Studio', str(tag))
            if resp.get('crash'):
                continue

            up_count_verified = resp.get('count', 0)
            print(
                f'{tag} {up_count_verified}/{len(filepaths)} confirmed files uploaded {time.perf_counter() - up_start} secs'
            )
            if resp.get('count') == len(filepaths):
                up_arrived = True
                break
            time.sleep(2)

        if up_arrived is False:
            print(f'verify upload failed {len(filepaths)} - {up_count_verified} files missing')
            print('30 seconds not enough time to verify?')

        # share files to other workspaces
        files_failed_sharing: int = 0
        for fp in filepaths:
            resp = self.API.wksp_share_file('Studio', fp, targetUsers=self.API.auth_username)
            if resp.get('crash'):
                print(f'share crash skipping {fp}')
                files_failed_sharing += 1

        # verify shared files arrived to determine test case can pass
        share_arrived: bool = False
        start_share: float = time.perf_counter()
        # TODO verify file share arrived to all non studio workspaces
        diffs = set()
        while share_arrived is False and time.perf_counter() - start_share < 180:
            resp = self.API.wksp_files(wksp_not_studio, str(tag))
            filenames_verified: set[str] = {f['filename'] for f in resp['files']}
            diffs: set[str] = set(filenames).symmetric_difference(filenames_verified)
            if resp.get('count') == up_count_verified and len(diffs) == 0:
                share_arrived = True
                break
            elif resp.get('count', 0) > up_count_verified:
                # BUG there might be file share retry logic
                # 1156398951931738_1.txt failed to share due to 500/504 issue but it showed up 5mins later
                # 1156398951931738_1_2022-10-15T021756Z.txt server tried more than once and created a duplicate!
                break
            time.sleep(2)

        if share_arrived:
            test_result = True
        else:
            print(f'verify share file diff: {len(diffs)}\n{sorted(diffs)}')

        # cleanup: remove files used to share out
        self.API.wksp_folder_delete('Studio', f'My Files/{tag}', force=True)

        # cleanup: remove files shared to other workspaces
        share_folders: list[str] = ['Sent to Me', 'sent_to_me']
        for ws in wksp_names:
            for share_folder in share_folders:
                resp = self.API.wksp_files(ws, share_folder)
                if resp.get('count') == 0:
                    continue
                for fn in filenames:
                    self.API.wksp_file_delete(ws, f'{share_folder}/{self.API.auth_username}/{fn}')

        self.assertTrue(test_result)

    def test_wksp_share_folder(self) -> None:
        '''share a subtree from a workspace to all other workspaces of a user/self'''

        if self.API.auth_username is None:
            self.skipTest('test_wksp_share_folder requires a username')

        resp = self.API.wksp_share_folder(
            self.WKSP, dir_path=self.dir_testdata_remote, targetUsers=self.API.auth_username
        )
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(len(resp.keys()), 8)
        self.assertIsInstance(resp['errored'], list)
        self.assertEqual(len(resp['errored']), 0)
        self.assertIsInstance(resp['erroredCount'], int)
        self.assertIsInstance(resp['jobs'], list)
        self.assertEqual(len(resp['jobs']), self.API.account_workspace_count - 1)
        for j in resp['jobs']:
            self.assertIsInstance(j['jobKey'], str)
            self.assertIsInstance(j['result'], str)
            self.assertEqual(j['result'], 'success')
        self.assertEqual(resp['jobsCount'], self.API.account_workspace_count - 1)
        self.assertIsInstance(resp['message'], str)
        self.assertEqual(resp['message'], 'Share Accepted')
        self.assertIsInstance(resp['sourceFileInfo'], dict)
        self.assertEqual(len(resp['sourceFileInfo'].keys()), 1)
        self.assertIsInstance(resp['sourceFileInfo']['directoryPath'], str)
        self.assertEqual(resp['sourceFileInfo']['directoryPath'], self.dir_testdata_remote)
        self.assertEqual(resp['targetUsers'], self.API.auth_username)


if __name__ == '__main__':
    # !! TODO update module docstring to set your user defaults !!
    # apikey replace YOUR_USERNAME, YOUR_PASSWORD
    # appkey replace YOUR_USERNAME, YOUR_APPLICATION_KEY, and set auth_legacy to False

    args: dict = docopt(__doc__)
    TestApi.APPKEY = args.get('--appkey')
    TestApi.AUTH_LEGACY = args.get('--authlegacy', '').lower() == 'true'
    TestApi.USERNAME = args.get('--user')
    TestApi.USERPASS = args.get('--pass')
    TestApi.WKSP = args.get('--wksp', 'Studio')
    unittest.main(__name__, argv=['main'])
