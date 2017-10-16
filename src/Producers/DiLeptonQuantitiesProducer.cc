
#include "Artus/Consumer/interface/LambdaNtupleConsumer.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/DiLeptonQuantitiesProducer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/Quantities.h"


void DiLeptonQuantitiesProducer::Init(setting_type const& settings, metadata_type& metadata)
{
	ProducerBase<HttTypes>::Init(settings, metadata);
	
	// add possible quantities for the lambda ntuples consumers
	LambdaNtupleConsumer<HttTypes>::AddRMFLVQuantity(metadata, "diLepLV", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem;
	});
	LambdaNtupleConsumer<HttTypes>::AddRMFLVQuantity(metadata, "genDiLepLV", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonGenSystem;
	});
	LambdaNtupleConsumer<HttTypes>::AddBoolQuantity(metadata, "genDiLepFound", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonGenSystemFound;
	});
	LambdaNtupleConsumer<HttTypes>::AddRMFLVQuantity(metadata, "genDiTauLV", [](event_type const& event, product_type const& product) {
		return product.m_diTauGenSystem;
	});
	LambdaNtupleConsumer<HttTypes>::AddBoolQuantity(metadata, "genDiTauFound", [](event_type const& event, product_type const& product) {
		return product.m_diTauGenSystemFound;
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepPt", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepEta", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepPhi", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMass", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMt", [](event_type const& event, product_type const& product) {
		return Quantities::CalculateMt(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepGenMass", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonGenSystem.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "mt_tt", [](event_type const& event, product_type const& product) {
		return Quantities::CalculateMtH2Tau(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4);
	});
	
	float smearing = settings.GetMassSmearing();
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMassSmearUp", [smearing](event_type const& event, product_type const& product) {
		double recoGenMassDiff = (product.m_diLeptonSystem.mass() - product.m_diLeptonGenSystem.mass());
		return product.m_diLeptonGenSystem.mass() + (recoGenMassDiff * (1.0 + smearing));
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMassSmearDown", [smearing](event_type const& event, product_type const& product) {
		float recoGenMassDiff = (product.m_diLeptonSystem.mass() - product.m_diLeptonGenSystem.mass());
		return product.m_diLeptonGenSystem.mass() + (recoGenMassDiff * (1.0 - smearing));
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetPt", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonPlusMetSystem.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetEta", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonPlusMetSystem.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetPhi", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonPlusMetSystem.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetMass", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonPlusMetSystem.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetMt", [](event_type const& event, product_type const& product) {
		return Quantities::CalculateMt(product.m_diLeptonSystem, product.m_met.p4);
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "pZetaVis", [](event_type const& event, product_type const& product) {
		return product.pZetaVis;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "pZetaMiss", [](event_type const& event, product_type const& product) {
		return product.pZetaMiss;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "pZetaMissVis", [](event_type const& event, product_type const& product) {
		return product.pZetaMissVis;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "collinearMass", [](event_type const& event, product_type const& product) {
		return product.m_col;
	});

	//Variables used for HWW, some just for testing
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepDPhi", [](event_type const& event, product_type const& product) {
		return product.diLepDPhi;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepCosDPhi", [](event_type const& event, product_type const& product) {
		return cos(product.m_flavourOrderedLeptons.at(1)->p4.Phi() - product.m_flavourOrderedLeptons.at(0)->p4.Phi());
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetCosDPhi", [](event_type const& event, product_type const& product) {
		return cos(product.m_diLeptonSystem.Phi() - product.m_met.p4.Phi());
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepTheta", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.Theta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepDTheta", [](event_type const& event, product_type const& product) {
		return std::abs(product.m_flavourOrderedLeptons.at(1)->p4.Theta() - product.m_flavourOrderedLeptons.at(0)->p4.Theta());
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepAbsCosTheta", [](event_type const& event, product_type const& product) {
		return std::abs(cos(product.m_diLeptonSystem.Theta()));
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepEta", [](event_type const& event, product_type const& product) {
		return product.m_diLeptonSystem.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepCosThetaStar", [](event_type const& event, product_type const& product) {
		return product.diLepCosThetaStar;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepAngle", [](event_type const& event, product_type const& product) {
		return product.diLepAngle;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetAngle", [](event_type const& event, product_type const& product) {
		return product.diLepMetAngle;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity(metadata, "diLepMetMtImp", [](event_type const& event, product_type const& product) {
		return sqrt(pow(product.m_diLeptonSystem.P()+product.m_met.p4.Pt(),2)-product.m_diLeptonPlusMetSystem.P2());
		// Using "product.m_met.p4.Pt()" instead of "product.m_met.p4.E()" because E is sometimes 0.
	});
}

void DiLeptonQuantitiesProducer::Produce(event_type const& event, product_type& product,
	                                     setting_type const& settings, metadata_type const& metadata) const
{
	assert(product.m_metUncorr);
	assert(product.m_flavourOrderedLeptons.size() >= 2);

	product.m_diLeptonSystem = (product.m_flavourOrderedLeptons[0]->p4 + product.m_flavourOrderedLeptons[1]->p4);
	product.m_diLeptonPlusMetSystem = (product.m_diLeptonSystem + product.m_met.p4);
	
	product.m_diLeptonGenSystemFound = true;
	product.m_diTauGenSystemFound = true;
	for (size_t leptonIndex = 0; leptonIndex < 2; ++leptonIndex)
	{
		KGenParticle* genParticle = product.m_flavourOrderedGenLeptons.at(leptonIndex);
		if (genParticle)
		{
			product.m_diLeptonGenSystem += genParticle->p4;
		}
		else
		{
			product.m_diLeptonGenSystemFound = false;
		}
		
		KGenTau* genTau = SafeMap::GetWithDefault(product.m_genTauMatchedLeptons, product.m_ptOrderedLeptons.at(1), static_cast<KGenTau*>(nullptr));
		if (genTau)
		{
			product.m_diTauGenSystem += genTau->p4;
		}
		else
		{
			product.m_diTauGenSystemFound = false;
		}
	}
	if (! product.m_diLeptonGenSystemFound)
	{
		product.m_diLeptonGenSystem = DefaultValues::UndefinedRMFLV;
	}
	if (! product.m_diTauGenSystemFound)
	{
		product.m_diTauGenSystem = DefaultValues::UndefinedRMFLV;
	}
	
	// collinear approximation
	// reconstruct tau momenta assuming that the neutrinos fly collinear to the taus
	// HiggsAnalysis/KITHiggsToTauTau/doc/collinear_approximation.nb
	double p1x = product.m_flavourOrderedLeptons[0]->p4.Px();
	double p1y = product.m_flavourOrderedLeptons[0]->p4.Py();
	double p2x = product.m_flavourOrderedLeptons[1]->p4.Px();
	double p2y = product.m_flavourOrderedLeptons[1]->p4.Py();
	double pmx = product.m_met.p4.Px();
	double pmy = product.m_met.p4.Py();
	double ratioVisToTau1 = (p1y*p2x - p1x*p2y + p2y*pmx - p2x*pmy) / (p1y*p2x - p1x*p2y);
	double ratioVisToTau2 = (p1y*p2x - p1x*p2y - p1y*pmx + p1x*pmy) / (p1y*p2x - p1x*p2y);
	double xvist1 = (pow(pow(p1x,2.0) + pow(p1y,2.0),0.5))/((pow(pow(p1x,2.0) + pow(p1y,2.0),0.5))+(pow(pow(pmx,2.0)+pow(pmy,2.0),0.5)));
	double xvist2 = (pow(pow(p2x,2.0) + pow(p2y,2.0),0.5))/((pow(pow(p2x,2.0) + pow(p2y,2.0),0.5))+(pow(pow(pmx,2.0)+pow(pmy,2.0),0.5)));

	product.m_flavourOrderedTauMomentaCA.clear();
	if (ratioVisToTau1 >= 0.0 && ratioVisToTau2 >= 0.0)
	{
		product.m_flavourOrderedTauMomentaCA.push_back(RMFLV(product.m_flavourOrderedLeptons[0]->p4 / ratioVisToTau1));
		product.m_flavourOrderedTauMomentaCA.push_back(RMFLV(product.m_flavourOrderedLeptons[1]->p4 / ratioVisToTau2));
		product.m_diTauSystemCA = product.m_flavourOrderedTauMomentaCA[0] + product.m_flavourOrderedTauMomentaCA[1];
		product.m_validCollinearApproximation = true;	
	}
	else
	{
		product.m_validCollinearApproximation = false;
	}
	
	if (product.m_flavourOrderedLeptons.at(0)->flavour() == KLeptonFlavour::TAU && product.m_flavourOrderedLeptons.at(1)->flavour() != KLeptonFlavour::TAU)
	{
		product.m_col = product.m_diLeptonSystem.mass()/std::sqrt(xvist1);
	}
	else if (product.m_flavourOrderedLeptons.at(0)->flavour() != KLeptonFlavour::TAU && product.m_flavourOrderedLeptons.at(1)->flavour() == KLeptonFlavour::TAU)
	{
		product.m_col = product.m_diLeptonSystem.mass()/std::sqrt(xvist2);
	}

	product.pZetaVis = Quantities::PZetaVis(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4);
	product.pZetaMiss = Quantities::PZetaMissVis(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4,
	                                             product.m_met.p4, 0.0);
	product.pZetaMissVis = Quantities::PZetaMissVis(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4,
	                                                product.m_met.p4, 0.85);

	//Variables used for HWW, some just for testing
	product.diLepDPhi = product.m_flavourOrderedLeptons.at(1)->p4.Phi() - product.m_flavourOrderedLeptons.at(0)->p4.Phi();
	if (product.diLepDPhi > acos(-1)){
		product.diLepDPhi = product.diLepDPhi - (2*acos(-1));
	}
	if (product.diLepDPhi < -1*acos(-1)){
		product.diLepDPhi = product.diLepDPhi + (2*acos(-1));
	}
	product.diLepRestFrame = product.m_diLeptonSystem.BoostToCM();
	ROOT::Math::Boost boostedHighptLepton(product.diLepRestFrame);
	product.diLepCosThetaStar = Quantities::cosptAngle(boostedHighptLepton * product.m_ptOrderedLeptons[0]->p4, product.m_diLeptonSystem);
	product.diLepAngle = Quantities::cosptAngle(product.m_flavourOrderedLeptons[0]->p4, product.m_flavourOrderedLeptons[1]->p4);
	product.diLepMetAngle = Quantities::cosptAngle(product.m_diLeptonSystem, product.m_met.p4);
}
