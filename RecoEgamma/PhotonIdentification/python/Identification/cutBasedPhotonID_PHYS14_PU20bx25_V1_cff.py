
from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

# Common functions and classes for ID definition are imported here:
from RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_tools import *

#
# This is the first version of PHYS14 cuts, optimized on  PHYS14 samples. 
#
# The ID cuts below are optimized IDs for PHYS14 Scenario PU 20, bx 25ns
# The cut values are taken from the twiki:
#       https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedPhotonIdentificationRun2#PHYS14_selections_PU20_bunch_cro
#       (where they may not stay, if a newer version of cuts becomes available for these
#        conditions)
# See also the presentation explaining these working points (this will not change):
#       https://indico.cern.ch/event/367863/contribution/0/material/slides/0.pdf

#
# First, define cut values
#

# Loose working point Barrel and Endcap
idName = "cutBasedPhotonID-PHYS14-PU20bx25-V1-standalone-loose"
WP_Loose_EB = WorkingPoint_V1(
    idName    ,  # idName
    0.048     ,  # hOverECut
    0.0106    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    2.56      ,  # absPFChaHadIsoWithEACut_C1
    0         ,  # absPFChaHadIsoWithEACut_C2
    3.74      ,  # absPFNeuHadIsoWithEACut_C1
    0.0025    ,  # absPFNeuHadIsoWithEACut_C2
    2.68      ,  # absPFPhoIsoWithEACut_C1
    0.001        # absPFPhoIsoWithEACut_C2
    )

WP_Loose_EE = WorkingPoint_V1(
    idName    ,  #idName
    0.069     ,  # hOverECut
    0.0266    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    3.12      ,  # absPFChaHadIsoWithEACut_C1
    0.00      ,  # absPFChaHadIsoWithEACut_C2
    17.11     ,  # absPFNeuHadIsoWithEACut_C1
    0.0118    ,  # absPFNeuHadIsoWithEACut_C2
    2.70      ,  # absPFPhoIsoWithEACut_C1
    0.0059       # absPFPhoIsoWithEACut_C2
    )

# Medium working point Barrel and Endcap
idName = "cutBasedPhotonID-PHYS14-PU20bx25-V1-standalone-medium"
WP_Medium_EB = WorkingPoint_V1(
    idName    ,  # idName
    0.032     ,  # hOverECut
    0.0101    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    1.90      ,  # absPFChaHadIsoWithEACut_C1
    0.00      ,  # absPFChaHadIsoWithEACut_C2
    2.96      ,  # absPFNeuHadIsoWithEACut_C1
    0.0025    ,  # absPFNeuHadIsoWithEACut_C2
    1.39      ,  # absPFPhoIsoWithEACut_C1
    0.001        # absPFPhoIsoWithEACut_C2
    )

WP_Medium_EE = WorkingPoint_V1(
    idName    ,  #idName
    0.0166    ,  # hOverECut
    0.0264    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    1.95      ,  # absPFChaHadIsoWithEACut_C1
    0.00      ,  # absPFChaHadIsoWithEACut_C2
    4.42      ,  # absPFNeuHadIsoWithEACut_C1
    0.0118    ,  # absPFNeuHadIsoWithEACut_C2
    1.89      ,  # absPFPhoIsoWithEACut_C1
    0.0059       # absPFPhoIsoWithEACut_C2
    )

# Tight working point Barrel and Endcap
idName = "cutBasedPhotonID-PHYS14-PU20bx25-V1-standalone-tight"
WP_Tight_EB = WorkingPoint_V1(
    idName    ,  # idName
    0.0099    ,  # hOverECut
    0.0099    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    1.86      ,  # absPFChaHadIsoWithEACut_C1
    0.00      ,  # absPFChaHadIsoWithEACut_C2
    2.64      ,  # absPFNeuHadIsoWithEACut_C1
    0.0025    ,  # absPFNeuHadIsoWithEACut_C2
    1.20      ,  # absPFPhoIsoWithEACut_C1
    0.001        # absPFPhoIsoWithEACut_C2
    )

WP_Tight_EE = WorkingPoint_V1(
    idName    ,  #idName
    0.015     ,  # hOverECut
    0.0263    ,  # full5x5_SigmaIEtaIEtaCut
    # Isolation cuts are generally absIso < C1 + pt*C2
    1.68      ,  # absPFChaHadIsoWithEACut_C1
    0.00      ,  # absPFChaHadIsoWithEACut_C2
    4.42      ,  # absPFNeuHadIsoWithEACut_C1
    0.0118    ,  # absPFNeuHadIsoWithEACut_C2
    1.03      ,  # absPFPhoIsoWithEACut_C1
    0.0059       # absPFPhoIsoWithEACut_C2
    )

#
# Second, set up VID configuration for all cuts
#
cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_loose  = configureVIDCutBasedPhoID_V1 ( WP_Loose_EB, WP_Loose_EE)
cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_medium = configureVIDCutBasedPhoID_V1 ( WP_Medium_EB, WP_Medium_EE)
cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_tight  = configureVIDCutBasedPhoID_V1 ( WP_Tight_EB, WP_Tight_EE)

#
# The MD5 sum numbers below reflect the exact set of cut variables
# and values above. If anything changes, one has to 
# 1) comment out the lines below about the registry, 
# 2) run "calculateMD5 <this file name> <one of the VID config names just above>
# 3) update the MD5 sum strings below and uncomment the lines again.
#

central_id_registry.register(cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_loose.idName,
                             'f5e8afd610fee496483d2ae702cfc93f')
central_id_registry.register(cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_medium.idName,
                             '0cf17a9d445fb70d3fbde377f2e311ba')
central_id_registry.register(cutBasedPhotonID_PHYS14_PU20bx25_V1_standalone_tight.idName,
                             'a49864a3837a3db7e57424f809938849')