import os
from abc import ABC, abstractmethod
from pathlib import Path

import lumipy as lm
import pandas as pd
from finbourne_lab.common.observation import Observation


class BaseRecorder(ABC):
    """Base class for all data recorder classes in Finbourne Lab.

    """

    def __init__(self, chunk_size: int):
        """Constructor of the BaseRecorder class.

        Args:
            chunk_size (int): the max size of an experiment's staging area before it's written out.

        """

        self.chunk_size = chunk_size
        self.staging = {}

    @abstractmethod
    def _send(self, name: str) -> None:
        """Send all data corresponding to the given name to the data store.

        Args:
            name (str): the name of the experiment to send out.

        """
        raise NotImplementedError()

    def put(self, obs: Observation) -> None:
        """Add an observation to the staging area. When there are self.chunk_size-many or more send will be triggered.

        Args:
            obs (Observation): the observation to add.

        """

        name = obs['name']

        if name not in self.staging:
            self.staging[name] = []

        obs_list = self.staging[name]

        obs_list.append(obs)

        if len(obs_list) >= self.chunk_size:
            self._send(name)

    def flush(self) -> None:
        """Send all staged data to the data store.

        """
        for name, obs_list in self.staging.items():
            if len(obs_list) == 0:
                continue

            self._send(name)

    def put_all(self, queue) -> None:
        """Empty out the queue into the staging area.

        Args:
            queue (Queue): the multiprocessing Queue instance that the experiments are pushing observations to.

        """
        while not queue.empty():
            obs = queue.get()
            self.put(obs)

    @abstractmethod
    def get_df(self, name: str) -> pd.DataFrame:
        """Get the data for a given experiment name from the data store as a pandas dataframe.

        Args:
            name (str): the name of the experiment's data to fetch.

        Returns:
            DataFrame: the corresponding data as a DataFrame
        """
        raise NotImplementedError()


class FileRecorder(BaseRecorder):
    """Recorder for writing experiment data to a local directory.

    """

    def __init__(self, directory: str, chunk_size: int = 5):
        """Constructor for the FileRecorder class.

        Args:
            directory (str): path of the write directory.
            chunk_size (int): the max size of an experiment's staging area before it's written out.

        """
        self.directory = directory
        Path(directory).mkdir(parents=True, exist_ok=True)

        super().__init__(chunk_size)

    def _send(self, name):
        df = pd.DataFrame(self.staging[name])
        fpath = f'{self.directory}/{name}.csv'
        df.to_csv(fpath, index=False, mode='a', header=not os.path.exists(fpath))
        self.staging[name] = []

    def get_df(self, name: str) -> pd.DataFrame:
        """Get the data for a given experiment name from a local file as a pandas dataframe.

        Args:
            name (str): the name of the experiment's data to fetch.

        Returns:
            DataFrame: the corresponding data as a DataFrame
        """
        fpath = f'{self.directory}/{name}.csv'
        return pd.read_csv(fpath)


class DriveRecorder(BaseRecorder):
    """Recorder for writing experiment data to a drive directory.

    """

    def __init__(self, atlas, directory: str, chunk_size: int = 5):
        """Constructor for the DriveRecorder class.

        Args:
            atlas (Atlas): atlas to use when writing to drive.
            directory (str): directory in drive to write to.
            chunk_size (int): the max size of an experiment's staging area before it's written out.

        """
        self.directory = directory
        self.files = atlas.drive_file
        self.write = atlas.drive_saveas
        self.read = atlas.drive_csv
        super().__init__(chunk_size)

    def _file_exists(self, name):
        f = self.files(root_path=self.directory)
        df = f.select('*').where(f.name == f'{name}.csv').go(quiet=True)
        return df.shape[0] == 1

    def _send(self, name):
        df = pd.DataFrame(self.staging[name])
        tv = lm.from_pandas(df)

        if self._file_exists(name):
            csv = self.read(file=f'{self.directory}/{name}.csv').select('*')
            tv2 = csv.union(tv.select('*')).to_table_var()
            q = self.write(tv2, type='csv', path=self.directory, file_names=name).select('*')
        else:
            q = self.write(tv, type='csv', path=self.directory, file_names=name).select('*')

        q.go_async()

    def get_df(self, name):
        """Get the data for a given experiment name from a drive file as a pandas dataframe.

        Args:
            name (str): the name of the experiment's data to fetch.

        Returns:
            DataFrame: the corresponding data as a DataFrame
        """
        csv = self.read(file=f'{self.directory}/{name}.csv', infer_type_row_count=10)
        return csv.select('*').go(quiet=True)
