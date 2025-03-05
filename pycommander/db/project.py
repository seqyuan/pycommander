from dataclasses import dataclass
from pandas import Series
import os
import subprocess
from pycommander._utils import _get_yaml_data, generate_shell, decorate_shell


@dataclass
class project:
    """
    Class for project status update
    """
    proid: str
    ptype: str
    workdir: str
    dirstat: str
    info: str
    data: str
    autoconf: str
    qsubsge_sh: str
    pid: str
    p_args: str
    stime: str
    etime: str
    pstat: str
    run_num: str

    @classmethod
    def from_series(cls, series: Series):
        return cls(
            proid=series['proid'],   # 按Series索引名提取
            ptype=series['ptype'],
            workdir=series['workdir'],
            dirstat=series['dirstat'],
            info=series['info'],
            data=series['data'],
            autoconf=series['autoconf'],
            qsubsge_sh=series['qsubsge_sh'],
            pid=series['pid'],
            p_args=series['p_args'],
            stime=series['stime'],
            etime=series['etime'],
            pstat=series['pstat'],
            run_num=series['run_num'],
        )

    def check_dirstat(self) -> str:
        if self.dirstat == 'Y':
            return
        if os.path.isdir(f'{self.workdir}/info') and os.path.isdir(f'{self.workdir}/Filter') and os.path.isdir(f'{self.workdir}/Analysis'):
            self.dirstat = 'Y'

    def check_info(self, infofile: str = 'info/info.xlsx') -> str:
        if self.info == 'Y':
            return
        if os.path.isfile(f'{self.workdir}/{infofile}'):
            self.info = 'Y'

    def check_data(self, datasign: str = "Filter/GO.sign") -> str:
        if self.data == 'Y':
            return
        if os.path.isfile(f'{self.workdir}/{datasign}'):
            self.data = 'Y'
            
    def autoconf_exe(self, analysis_dir: str = 'Analysis'):
        if self.autoconf == 'Y' or self.autoconf == 'err':
            return
        if self.info == "Y" and self.data == 'Y':
            conf = _get_yaml_data('~/.pycommander/cmd.yaml')
            aufoconf_programe = conf["trackc"][self.ptype]

            shell = f'{self.workdir}/{analysis_dir}/autoconf.sh'
            content = f'{aufoconf_programe} -in {self.workdir}/{analysis_dir} -t {self.ptype}'

            try:
                generate_shell(shell, content)
                self.autoconf == 'Y'
            except Exception as e:
                #with open(f'{shell}.e', "w") as f:
                #    f.write(e)
                self.autoconf == 'err'
                return

        tss = subprocess.Popen(f"sh {shell}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdot, stder = tss.communicate()
        autoconf_stdout, autoconf_stderr = str(stdot,'utf-8'), str(stder,'utf-8')
        prosper = autoconf_stderr.split('\n')
        if len(prosper) >= 2:
            prosper = prosper[-2]
        else:
            prosper = '-'





        if prosper == "Live_long_and_prosper":
            if self.qsub_first != 'yes':
                decorate_shell(f'{self.workdir}/{analysis_dir}/autoconf.sh')
                self.autoconf = 'Y'
        else:
            self.autoconf = 'err'
            # self.type_subprojectID_qsub_sge_generate = False







