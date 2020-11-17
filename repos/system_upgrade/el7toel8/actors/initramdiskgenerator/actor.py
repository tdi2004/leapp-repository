from leapp.actors import Actor
from leapp.libraries.actor import initramgen
from leapp.models import (
    BootContent,
    RequiredUpgradeInitramPackages,  # deprecated
    TargetUserSpaceInfo,
    TargetUserSpaceUpgradeTasks,
    UpgradeDracutModule,  # deprecated
    UpgradeInitramfsTasks,
    UsedTargetRepositories,
)
from leapp.tags import InterimPreparationPhaseTag, IPUWorkflowTag


class InitramDiskGenerator(Actor):
    """
    Creates the upgrade initram disk

    Creates an initram disk within a systemd-nspawn container using the target
    system userspace, including new kernel. The creation of the initram disk
    can be influenced with the UpgradeInitramfsTasks message (e.g. specifying
    what files or dracut modules should be installed in the upgrade initramfs)

    See the UpgradeInitramfsTasks model for more details.
    """

    name = 'initram_disk_generator'
    consumes = (
        RequiredUpgradeInitramPackages,  # deprecated
        TargetUserSpaceInfo,
        TargetUserSpaceUpgradeTasks,
        UpgradeDracutModule,  # deprecated
        UpgradeInitramfsTasks,
        UsedTargetRepositories,
    )
    produces = (BootContent,)
    tags = (IPUWorkflowTag, InterimPreparationPhaseTag)

    def process(self):
        initramgen.process()
