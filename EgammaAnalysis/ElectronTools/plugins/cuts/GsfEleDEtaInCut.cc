#include "PhysicsTools/SelectorUtils/interface/CutApplicatorBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"

class GsfEleDEtaInCut : public CutApplicatorBase {
public:
  GsfEleDEtaInCut(const edm::ParameterSet& c) :
    CutApplicatorBase(c),
    _dEtaInCutValueEB(c.getParameter<double>("dEtaInCutValueEB")),
    _dEtaInCutValueEE(c.getParameter<double>("dEtaInCutValueEE")),
    _barrelCutOff(c.getParameter<double>("barrelCutOff")){    
  }
  
  result_type operator()(const reco::GsfElectronRef&) const override final;

  CandidateType candidateType() const override final { 
    return ELECTRON; 
  }

private:
  const double _dEtaInCutValueEB,_dEtaInCutValueEE,_barrelCutOff;
};

DEFINE_EDM_PLUGIN(CutApplicatorFactory,
		  GsfEleDEtaInCut,
		  "GsfEleDEtaInCut");

CutApplicatorBase::result_type 
GsfEleDEtaInCut::
operator()(const reco::GsfElectronRef& cand) const{  
  const float dEtaInCutValue = 
    ( std::abs(cand->superCluster()->position().eta()) < _barrelCutOff ? 
      _dEtaInCutValueEB : _dEtaInCutValueEE );
  return std::abs(cand->deltaEtaSuperClusterTrackAtVtx()) < dEtaInCutValue;
}
