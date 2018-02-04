***************************************
Abaqus analysis batch queue definitions
***************************************

This module provides Abaqus analysis batch queue definitions.
Currently only definitions for `SLURM <https://slurm.schedmd.com>`_
are implemented.


Installation
============

You can simply install the ``mecmi`` module in the abaqus ``site-packages``
directory::

  abaqus python setup.py install

or in an alternative location::

  abaqus python setup.py install --install-lib <LIBDIR>


Use
===

Add the following lines to your ``abaqus_v6.env`` file::

  import mecmi
  queues = {'slurm': mecmi.MecMi(mecmi.SlurmJob),}

or, if you installed in an alternative location not on the
Abaqus ``sys.path``::

  import site
  site.addsitedir('<LIBDIR>')
  import mecmi
  queues = {'slurm': mecmi.MecMi(mecmi.SlurmJob),}

Running ::

  abaqus job=myjob queue=slurm

will produce a shell script ``myjob.sh`` that has to be submitted
with ``sbatch``, e.g.::

  sbatch --partition=mypartition myjob.sh


