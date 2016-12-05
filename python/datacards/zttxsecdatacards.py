# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import CombineHarvester.CombineTools.ch as ch

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards


class ZttXsecDatacards(datacards.Datacards):
	def __init__(self, cb=None, model='default'):
		super(ZttXsecDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["inclusive"]],
					#categories=["mt_"+category for category in ["0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZTT", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)
			#if "taueff" not in model:
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Tau ES
			self.cb.cp().channel(["mt"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			
			# Top pT reweight
			self.cb.cp().channel(["mt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)
		
			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=["et_"+category for category in ["inclusive"]],
					#categories=["et_"+category for category in ["0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["et"]).process(["ZTT", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.electron_efficieny_syst_args)
			#if "taueff" not in model:
			self.cb.cp().channel(["et"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)
			self.cb.cp().channel(["et"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["et"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Tau ES
			self.cb.cp().channel(["et"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_tight_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			
			# Top pT reweight
			self.cb.cp().channel(["et"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)
		
			# ======================================================================
			# EM channel
			self.add_processes(
					channel="em",
					categories=["em_"+category for category in ["incl"]],
					bkg_processes=["ZLL", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["em"]).process(["ZTT", "ZLL", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.electron_efficieny_syst_args)
			self.cb.cp().channel(["em"]).process(["ZTT", "ZLL", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["em"]).process(["TT"]).AddSyst(self.cb, *self.ttj_extrapol_syst_args)

			# Electron ES
			self.cb.cp().channel(["em"]).process(["ZTT", "TT", "W", "VV"]).AddSyst(self.cb, *self.ele_es_syst_args)

			# Muon ES
			self.cb.cp().channel(["em"]).process(["ZTT", "TT", "W", "VV"]).AddSyst(self.cb, *self.mu_es_syst_args)

			# Top pT reweight
			self.cb.cp().channel(["em"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)

			# ======================================================================
			# All channels
			#self.cb.cp().process(["ZTT"]).AddSyst(self.cb, "ZTT_uniform_2", "lnU", ch.SystMap()(2.0))
		
			# lumi
			self.cb.cp().process(["ZTT", "ZLL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)
		
			# cross section
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# signal acceptance/efficiency
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)

			# DY reweighting
			self.cb.cp().process(["ZTT", "ZL"]).AddSyst(self.cb, *self.dy_syst_args)

			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_args)
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()


class ZttEffDatacards(datacards.Datacards):
	def __init__(self, cb=None):
		super(ZttEffDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["tauidvtightpass", "tauidvtightfail"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZL", "ZJ", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)

			# mu->tau fake ES
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_es_syst_args)

			# Tau ES
			self.cb.cp().channel(["mt"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# b-tag efficiency and mistag
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT"]).AddSyst(self.cb, *self.btag_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT"]).AddSyst(self.cb, *self.btag_mistag_syst_args)

			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=["et_"+category for category in ["tauidpass", "tauidfail"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["et"]).process(["ZL", "ZJ", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.electron_efficieny_syst_args)

			# Tau ES
			self.cb.cp().channel(["et"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_tight_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# b-tag efficiency and mistag
			self.cb.cp().channel(["et"]).process(["ZTT", "TT"]).AddSyst(self.cb, *self.btag_efficieny_syst_args)
			self.cb.cp().channel(["et"]).process(["ZTT", "TT"]).AddSyst(self.cb, *self.btag_mistag_syst_args)

			# ======================================================================
			# All channels
			# lumi
			self.cb.cp().process(["ZTT", "ZLL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)
		
			# cross section
			self.cb.cp().process(["ZL", "ZJ"]).AddSyst(self.cb, *self.ztt_cross_section_syst_args)
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# signal acceptance/efficiency
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)

			# W+jets extrapolation
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)
			
			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_inclusive_args)
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()


class ZttLepTauFakeRateDatacards(datacards.Datacards):
	def __init__(self, cb=None):
		super(ZttLepTauFakeRateDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["antimutightpass", "antimutightfail"]],
					bkg_processes=["ZTT", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZL", "ZJ", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)
			
			# Tau ES
			self.cb.cp().channel(["mt"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)
			
			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=["et_"+category for category in ["antievloosepass", "antievloosefail"]],
					bkg_processes=["ZTT", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["et"]).process(["ZTT", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.electron_efficieny_syst_args)
			self.cb.cp().channel(["et"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)
			self.cb.cp().channel(["et"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)

			# Probe Tau ES
			self.cb.cp().channel(["et"]).process(["ZTT"]).AddSyst(self.cb, *self.probetau_es_syst_args)
			
			# Probe Electron ES
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.probeele_es_syst_args)
			
			# Tag Electron ES
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.tagele_es_syst_args)
			
			# Visible mass resolution
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.massres_syst_args)
		
			# additional nuisance for possible differences in Z -> ee norm., in addition to the Z->tautau norm.
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.zee_norm_syst_args)
			
			# ======================================================================
			# All channels
			# lumi
			self.cb.cp().process(["ZTT", "ZLL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)
		
			# cross section
			self.cb.cp().process(["ZTT", "ZL", "ZJ"]).AddSyst(self.cb, *self.ztt_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)
			
			# W+jets extrapolation
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)
			
			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_args)
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()


class ZttJetTauFakeFactorDatacards(datacards.Datacards):
	def __init__(self, cb=None, model='default'):
		super(ZttJetTauFakeFactorDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["inclusive"]],
					#categories=["mt_"+category for category in ["inclusive","0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					#categories=["mt_"+category for category in ["0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					bkg_processes=["ZL", "TTJT", "TTJL", "VVT", "VVL", "FF"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "VVT", "WJT", "ZTT"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "VVT", "WJT", "ZTT"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["WJT", "WJL"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Muon ES
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.mu_es_syst_args)

			# Tau ES
			self.cb.cp().channel(["mt"]).process(["TTJT", "VVT", "ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)
			#self.cb.cp().channel(["mt"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# MET scale
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resp_channel_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resp_syst_args)

			# MET resolution
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resol_channel_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resol_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["TTJL", "VVL", "WJL", "ZL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["TTJL", "VVL", "WJL", "ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# Top pT reweight
			self.cb.cp().channel(["mt"]).process(["TTJT", "TTJL"]).AddSyst(self.cb, *self.ttj_syst_args)
			
			# Fake-Factor (Jets faking Taus)
			#new
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_syst_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_syst_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_stat_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_stat_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_syst_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_syst_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_stat_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_stat_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_syst_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_syst_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_stat_category_args)
			self.cb.cp().channel(["mt"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_stat_args)


			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					#categories=["et_"+category for category in ["inclusive"]],
					categories=["et_"+category for category in ["inclusive","0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					#categories=["et_"+category for category in ["0jet","1jet_low","1jet_medium","1jet_high","2jet_vbf","1bjet","2bjet"]],
					bkg_processes=["ZL", "TTJT", "TTJL", "VVT", "VVL", "FF"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["90"]
			)
		
			# efficiencies
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.electron_efficieny_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "VVT", "WJT", "ZTT"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "VVT", "WJT", "ZTT"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)
			
			# extrapolation uncertainty
			self.cb.cp().channel(["et"]).process(["WJT", "WJL"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Electron ES
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.ele_es_syst_args)
			
			# Tau ES
			self.cb.cp().channel(["et"]).process(["TTJT", "VVT", "ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)
			#self.cb.cp().channel(["et"]).process(["ZTT"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# MET scale
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resp_channel_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resp_syst_args)

			# MET resolution
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resol_channel_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZTT"]).AddSyst(self.cb, *self.met_resol_syst_args)

			# fake-rate
			self.cb.cp().channel(["et"]).process(["TTJL", "VVL", "WJL", "ZL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["et"]).process(["TTJL", "VVL", "WJL", "ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# Top pT reweight
			self.cb.cp().channel(["et"]).process(["TTJT", "TTJL"]).AddSyst(self.cb, *self.ttj_syst_args)

			# Fake-Factor (Jets faking Taus)
			#new
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_syst_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_syst_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_stat_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_qcd_stat_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_syst_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_syst_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_stat_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_w_stat_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_syst_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_syst_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_stat_category_args)
			self.cb.cp().channel(["et"]).process(["FF"]).AddSyst(self.cb, *self.ff_tt_stat_args)
			
			
			# ======================================================================
			# All channels
			# lumi
			self.cb.cp().process(["ZTT", "ZLL", "TTJT", "TTJL", "VVT", "VVL", "WJT", "WJL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)
		
			# cross section
			#self.cb.cp().process(["ZL", "ZJ"]).AddSyst(self.cb, *self.ztt_cross_section_syst_args)
			self.cb.cp().process(["TTJT", "TTJL"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["VVT", "VVL"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["WJT", "WJL"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)
			
			# signal acceptance/efficiency
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)
			
			# DY reweighting
			self.cb.cp().process(["ZTT", "ZL"]).AddSyst(self.cb, *self.dy_syst_args)
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()
