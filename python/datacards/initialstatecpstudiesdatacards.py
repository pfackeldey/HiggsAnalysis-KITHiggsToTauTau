# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.categories as Categories
import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards
import HiggsAnalysis.KITHiggsToTauTau.datacards.smhttdatacards as smhttdatacards
import CombineHarvester.CombineTools.ch as ch

class InitialStateCPStudiesDatacards(smhttdatacards.SMHttDatacards):
                 
	def __init__(self, higgs_masses=["125"], ttbarFit=False, mmFit=False, year="", noJECuncSplit=False, cb=None, cp_study="ggh"):
		
		sm_signal_processes = ["ggH", "qqH"]#, "WH", "ZH"]
		cp_signal_processes = {
			"ggh" : ["ggHsm", "ggHps", "ggHmm"],
			"vbf" : ["qqHsm", "qqHps", "qqHmm"],
			"final" : [], # TODO
		}
		
		super(InitialStateCPStudiesDatacards, self).__init__(
				higgs_masses=higgs_masses,
				ttbarFit=ttbarFit,
				mmFit=mmFit,
				year=year,
				noJECuncSplit=noJECuncSplit,
				cb=cb,
				signal_processes=sm_signal_processes+cp_signal_processes.get(cp_study, [])
		)
		
		def remove_redundant_signal(obj):
			if not obj.signal():
				return False
			else:
				if any([key in obj.bin().lower() for key in ["twojet", "vbf"]]):
					if (cp_study == "ggh") and (obj.process() == "ggH"):
						return True
					elif (cp_study == "vbf") and (obj.process() == "qqH"):
						return True
					elif cp_study == "final":
						return False # TODO
					else:
						return False
				else:
					if any([obj.process() == key for key in cp_signal_processes.get("analysis", [])]):
						return True
					else:
						return False
		
		self.cb.FilterProcs(remove_redundant_signal)
		self.cb.FilterSysts(remove_redundant_signal)

