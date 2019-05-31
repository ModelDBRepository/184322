'''
Defines a class, Neuron473835796, of neurons from Allen Brain Institute's model 473835796

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473835796:
    def __init__(self, name="Neuron473835796", x=0, y=0, z=0):
        '''Instantiate Neuron473835796.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473835796_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Sst-IRES-Cre_Ai14_IVSCC_-173196.03.02.01_472471778_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473835796_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 29.76
            sec.e_pas = -92.1516036987
        
        for sec in self.axon:
            sec.cm = 1.54
            sec.g_pas = 0.000571087055933
        for sec in self.dend:
            sec.cm = 1.54
            sec.g_pas = 2.61144287962e-06
        for sec in self.soma:
            sec.cm = 1.54
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00238489
            sec.gbar_Ih = 3.70678e-06
            sec.gbar_NaTs = 0.490768
            sec.gbar_Nap = 0.000117117
            sec.gbar_K_P = 0.00347692
            sec.gbar_K_T = 0.000460258
            sec.gbar_SK = 0.000390759
            sec.gbar_Kv3_1 = 0.297742
            sec.gbar_Ca_HVA = 0.000786371
            sec.gbar_Ca_LVA = 0.0058102
            sec.gamma_CaDynamics = 0.00105086
            sec.decay_CaDynamics = 984.726
            sec.g_pas = 0.000133193
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

