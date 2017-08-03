import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *
from SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi import *
from SimTracker.TrackerHitAssociation.tpClusterProducer_cfi import *
from SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi import *
from RecoTracker.TransientTrackingRecHit.TTRHBuilders_cff import *
from RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi import *
from Geometry.TrackerNumberingBuilder.trackerTopology_cfi import *

from Validation.RecoTrack.trackingNtuple_cfi import *
from Validation.RecoTrack.TrackValidation_cff import *
from SimGeneral.TrackingAnalysis.trackingParticleNumberOfLayersProducer_cff import *
import Validation.RecoTrack.TrackValidation_cff as _TrackValidation_cff
import RecoTracker.IterativeTracking.ElectronSeeds_cff as _electron_cff

#_includeHits = True
_includeHits = False

_includeSeeds = True
#_includeSeeds = False

from CommonTools.RecoAlgos.trackingParticleRefSelector_cfi import trackingParticleRefSelector as _trackingParticleRefSelector
trackingParticlesIntime = _trackingParticleRefSelector.clone(
    signalOnly = False,
    intimeOnly = True,
    chargedOnly = False,
    tip = 1e5,
    lip = 1e5,
    minRapidity = -10,
    maxRapidity = 10,
    ptMin = 0,
)
trackingNtuple.trackingParticles = "trackingParticlesIntime"
trackingNtuple.trackingParticlesRef = True
trackingNtuple.includeAllHits = _includeHits
trackingNtuple.includeSeeds = _includeSeeds

def _filterForNtuple(lst):
    ret = []
    for item in lst:
        if "PreSplitting" in item:
            continue
        if "SeedsA" in item and item.replace("SeedsA", "SeedsB") in lst:
            ret.append(item.replace("SeedsA", "Seeds"))
            continue
        if "SeedsB" in item:
            continue
        if "SeedsPair" in item and item.replace("SeedsPair", "SeedsTripl") in lst:
            ret.append(item.replace("SeedsPair", "Seeds"))
            continue
        if "SeedsTripl" in item:
            continue
        ret.append(item)
    return ret

# Build seed tracks from the GSF tracks seeds
_seedProducers = ['electronMergedSeeds']
(_seedSelectors, trackingNtupleSeedSelectors) = _TrackValidation_cff._addSeedToTrackProducers(_seedProducers, globals())

trackingNtuple.seedTracks = _seedSelectors
trackingNtuple.tracks = cms.untracked.InputTag('electronGsfTracks')

# Matches to the original seeds defined in RecoTracker.IterativeTracking.ElectronSeeds_cff
_seedProducersOriginal = ['initialStepSeeds',
                          'highPtTripletStepSeeds',
                          'mixedTripletStepSeeds',
                          'pixelLessStepSeeds',
                          'tripletElectronSeeds',
                          'pixelPairElectronSeeds',
                          'stripPairElectronSeeds']
(_seedSelectorsOriginal, trackingNtupleSeedSelectorsOriginal) = _TrackValidation_cff._addSeedToTrackProducers(_seedProducersOriginal, globals())
trackingNtuple.seedTracksOriginal = _seedSelectorsOriginal
trackingNtuple.barrelSuperClusters = cms.untracked.InputTag("particleFlowSuperClusterECAL:particleFlowSuperClusterECALBarrel")
trackingNtuple.endcapSuperClusters = cms.untracked.InputTag("particleFlowSuperClusterECAL:particleFlowSuperClusterECALEndcapWithPreshower")
trackingNtupleSequence = cms.Sequence()

# reproduce hits because they're not stored in RECO
if _includeHits:
    trackingNtupleSequence += (
        siPixelRecHits +
        siStripMatchedRecHits
    )

if _includeSeeds:
    trackingNtupleSequence += trackingNtupleSeedSelectors
    trackingNtupleSequence += trackingNtupleSeedSelectorsOriginal

print 'Configuration for Ntuple finished'

trackingNtupleSequence += (
    # sim information
    trackingParticlesIntime +
    simHitTPAssocProducer +
    tpClusterProducer +
    quickTrackAssociatorByHits +
    trackingParticleNumberOfLayersProducer +
    # ntuplizer
    trackingNtuple
)

trackingPhase2PU140.toModify(trackingNtuple, # FIXME
  pixelDigiSimLink = cms.untracked.InputTag('simSiPixelDigis', "Pixel"),
  stripDigiSimLink = cms.untracked.InputTag(''),
  phase2OTSimLink = cms.untracked.InputTag('simSiPixelDigis', "Tracker")
)
