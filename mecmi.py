"""
queue definitions for Abaqus
"""

from __future__ import print_function
from pprint import pprint

# ABAQUS specific
import driverQueues
import driverConstants


class MecMi(driverQueues.Queue, object):
    """MecMi queue"""

    def __init__(self, jobfactory):
        super(MecMi, self).__init__()  # shoulb a no-op, but just in case ...
        self.jobfct = jobfactory

    def submit(self, options, env):
        if options.get('verbose'):
            print('---submit---')
        if options.get('verbose', 0) > 1:
            print('   ---options---')
            pprint(dict(options))
            print('   ---env---')
            pprint(dict(env))
        ntokens = self.getNumRequiredTokens(options)
        print("This job will require {} tokens".format(ntokens))
        job = self.jobfct(options, env, ntokens)
        return job.submit()

    def createScript(self, options):
        if options.get('verbose'):
            print('---createScript---')
        return super(MecMi, self).createScript(options)

    def validateExecHost(self, options):
        "undocumented method, called before createScript"
        if options.get('verbose'):
            print('---validateExecHost---')
        return super(MecMi, self).validateExecHost(options)


class SlurmJob(object):
    """class that encapsulates a Slurm batch job"""

    def __init__(self, options, env, ntokens):

        self.job = options['job']
        cpus = options.get('cpus', 1)

        abqcmd = '{abq} python -u {job}.com'.format(
            abq=env['ABA_COMMAND'], job=self.job)
        self.script = self.template.format(
            abqcmd=abqcmd, ntasks=cpus, job=self.job, ntokens=ntokens)

    def submit(self):
        script = self.job + '.sh'
        with open(script, 'w') as scriptfile:
            scriptfile.write(self.script)
        print("Please, submit '{}'".format(script))
        return 0

    template = """\
#!/bin/bash
#SBATCH --job-name={job}
#SBATCH --nodes=1
#SBATCH --ntasks={ntasks}
#SBATCH --out={job}.log
## #SBATCH --licenses=abqtokens:{ntokens}

function prompt {{
  echo --- $(date +'%Y-%m-%d %H:%M:%S %z') $@
  }}

function timereport {{
  tempnam=$(mktemp)
  times >> ${{tempnam}}
  mapfile -t times_a < ${{tempnam}}
  rm $tempnam
  times_s=$SECONDS
  prompt elapsed time: $(($times_s/60))m$(($times_s%60))s
  prompt cpu times: ${{times_a[1]}}
  }}
trap timereport EXIT

prompt job $SLURM_JOB_ID on $SLURM_CLUSTER_NAME/$SLURM_JOB_PARTITION

{abqcmd}

prompt job $SLURM_JOB_ID done
"""
