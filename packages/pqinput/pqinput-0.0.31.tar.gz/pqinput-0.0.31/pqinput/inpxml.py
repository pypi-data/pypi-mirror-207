#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:02:59 2023

@author: lucas

New INPUTMAKER with a "dictionary to XML" structure 

"""

'''TO IMPLEMENT
make laser part functional
'''
# %% Imports
from lxml import etree as et

# %% General functions
def dict2attr(element, params, tag=None):
    """ set the attributes for the xml element using a dict
        ignores keys as head, Opes and extras    """
    for key, value in params.items(): 
        if key not in ('head', 'Opes', 'extra'):
            element.set(str(key), str(value))
    if tag: element.tag = tag
    
def dict2elem(d, head=None, text_mode=False):
    """ transform a dictionary to a etree.element
    
    Args:
        d (dict) dictionary with attributes in key:value format
        _format: {'head':str, attr1:value1, ..., 'Opes':[dicts, ]}   
        head (string) node for the etree.Element
        text_mode (bool) choose the output format, etree.Element or etree.tostring
        
    Return: 
        string format of the etree.Element if text_mode else the etree._Element
        
        E.g.
        
        _In: dict2elem({'head':'node', 'attr1':'value1', 'Opes':[{'Op_element':'op'}]}, text_mode=True)
        
        _Out: b'<node attr1="value1"/>'
        
        # missing the operators part...
    """
    if not isinstance(d, dict):
        raise SyntaxError('Provide a dictionary to transform in a lxml element.')
    xml = et.Element(d['head']) if head==None else et.Element(head)
    # set the attributes of the lxml element removing the head and Operators part
    # [xml.set(str(key), str(value)) for key, value in d.items() if key not in ('head', 'Opes')]
    dict2attr(xml, d)
    return et.tostring(xml) if text_mode else xml

def subelem(supelem, params, head=None):
    """ create subelement for a lxml supelement using params dict
    Input:
        params; string - tail of subelement
                dict - tail with parameters
    Return: 
        lxml element; not mandatory
    """
    if not head:
        try: 
            params['head']
        except:
            raise SyntaxError('element head not provided')
    else: params['head'] = head
    sub = et.SubElement(supelem, params['head'])
    dict2attr(sub, params) 
    return sub

def printx(xmlelem): # works for any kind of lxml element, show is just for class
    print(et.tostring(xmlelem, pretty_print=True).decode())
    
    # Property methods
def typed_property(name): # Python Cookbook 3rd: 9.21
    storage_name = '_' + name
    
    @property
    def propriety(self): # lost in translation hehe
        # Print the property element 
        if not hasattr(self, storage_name): raise AttributeError(f'{name} attribute not defined.')
        return printx(getattr(self, storage_name))
    
    @propriety.setter
    def propriety(self, args):
        # modify key with new_value of propriedade using path 
        # args = [path, key, new_value] or "path_key_new_value"
        if isinstance(args, str): args = args.split('_') # single string format
        
        if len(args)==3:
            path, key, new_value = args
            element = getattr(self, storage_name).find(path)
            if element is None: raise AttributeError('setter path do not point to a defined attribute.')
            element.set(key, str(new_value))
        else:
            key, new_value = args
            getattr(self, storage_name).set(key, new_value)
        
        
        # READ MORE ABOUT XPATH AND IF ITS USEFUL
        
    return propriety
# %% 
'''-------------------------------------------------------------------------'''
'''                                Class                                    '''
'''-------------------------------------------------------------------------'''
class InpXML:
    """ InpXMl class for the creation of a qdng calculation input in xml format.
    requires the lxml.etree package
    
    Args:
        qdng_params (dict) parameters for the qdng calculation
        _format: {attr1:value1, attr2:value2, ... }
        * qdng [ -d output directory] [-p cpus] <input file> [var1=val1] ... [varN=valN]
        
    Attributes:
        qdng (etree._Element) root of the lxml tree
        program (etree._Element) program body: 
            either propa or eigen
        propag (etree._Element) branch of a program
        hamilt (etree._Element) branch a propagation: 
            subelement required for a Cheby propagation
        wavefunc (etree._Element) wavefunction body: 
            inclusion of initial wavefunctions for the calculations
    
    Properties:
        show: prints out the class text in readable xml format
        
        
    * comments from QDng documentation
    """
    qdng = et.Element("qdng") # Root of the XML tree: self.qdng, with the tag-headline 
    
    def __init__(self, qdng_params=None): # Initiate the input layout 
        if qdng_params: dict2attr(self.qdng, qdng_params)
        
    def __str__(self): # define string format for printing
        return f'{et.tostring(self.qdng, pretty_print=True).decode()}'    
    
    @property
    def show(self): # printing property
        '''Print out the full text in readable xml format
        Useful for debugging '''
        print(self)     
    
# %% 
    ''' METHODS '''
    ######################## Write file ########################
    def writexml(self, file_name='test_file', txt=False):
        """ Write the constructed lxml element to a XML file. """
        tree = et.ElementTree(self.qdng)
        if file_name.endswith('.txt'): 
            txt = True 
            file_name = file_name.strip('.txt')
        tree.write(file_name + ('.txt' if txt else '.xml'), pretty_print=True)
        
    def modify(self, path, key, new_value):
        self.qdng.find(path).set(key, str(new_value))
        
    def define_wavefunction(self, wfp):
        if wfp['type'] == 'file':
            wfel = et.Element('wf')
            wfel.set('file', wfp['file'])
            
        elif wfp['type'] == 'LC':
            wfel = et.Element('wf', name=wfp['type'])
            if 'normalize' in wfp.keys() and wfp['normalize']: wfel.set('normalize', 'true')
            for ind in range(wfp['states']):
                wfstate = et.SubElement(wfel, 'wf'+str(ind))
                wfstate.set('file', wfp['file'][ind])
            
        elif wfp['type'] == 'Multistate':
            wfel = et.Element('wf', name=wfp['type'])
            wfel.set('states', str(wfp['states'])) # hamiltonian define it later
            if 'normalize' in wfp.keys(): wfel.set('normalize', 'true')
            
            for ii, index in enumerate(wfp['index']):
                wfstate = et.SubElement(wfel, 'wf'+str(index), file=str(wfp['file'][ii]))
                if 'coeff2' in wfp.keys(): wfstate.set('coeff2', wfp['coeff2'][ii])
        else:
            raise SyntaxError('Wavefunction type not defined.')
        self._wavefunction = wfel
        return wfel
    
    # %% 
    """ Programs """
    def program(self, ptype, program_parameters, wf_parameters):
        """ Main program for the calculation. Either propagation or eigenfunction derivation.
                
        Args:
            ptype (string) type of program:
            _either 'propa' or 'eigen'
            program_parameters (dict) program parameters dictionary:
            _format: {'dt':num, 'steps':num, 'directory':str,'Nef':num, 'conv':num }
            wf_parameters (dict) wavefunction parameters dictionary:
            _format: {'name':str, 'states':num, 'file':[strs, ], 'normalize':True or None}
            
        """
        '''MAIN PROGRAM'''
        if not ptype in ['propa','eigen']: raise SyntaxError('Program not defined.')  
        self._program = subelem(self.qdng, program_parameters, ptype )
        # Create self._program as a lxml child element of qdng
        '''WAVEFUNCTION'''
        self.define_wavefunction(wf_parameters)
        # define wavefunction parameters
        
    prog = typed_property('program')    
    wavefunc = typed_property('wavefunction')
    
    # %% 
    """ Operators """
    def def_hamiltonian(self, Hp):    
        Hel = et.SubElement(self._propagation, 'hamiltonian')
        # Create a lxml element to be appended to the self.propag 
        
        if Hp['type'] == 'Sum': 
            Hel.set('name', Hp['type'])
            self.states = 1
            [subelem(Hel, opes) for opes in Hp['Opes']]
            # set hamiltonian of Sum type, creating subelements for each operator
        elif Hp['type'] == 'Multistate':
            Hel.set('name', Hp['type'])
            self.states = 0
            if None == Hp['Mels']:
                raise SyntaxError('Include states for the Multistate hamiltonian!')
            else:
                for mel in Hp['Mels'][:]:
                    # iterate through Hamiltonian matrix elements (mel)
                    self.states += 1
                    if len(mel['head'])<3: # easy way to set Hamiltonian matrix element 'mi.i'
                        mel['head'] = (f"m{mel['head'][1]}.{mel['head'][1]}")
                    elif len(mel['head'])==3:
                        mel['head'] = (f"m{mel['head'][1]}.{mel['head'][2]}")
                    branch = subelem(Hel, mel)
                    if 'Opes' in  mel.keys():
                        for ind in range(len(mel['Opes'])):
                            branch.append( dict2elem(mel['Opes'][ind])) 
        self._hamiltonian = Hel
        
    # %% 
    ''' Propagator '''
    def propagation(self, name, hamilt_params):
        """ Method for the wavefunction propagation. Return a etree.SubElement of previous defined program.
        
        Args:
            name (string) name of the propagation method:
                *GSPO, Cheby, *SIL, *Arnoldi (*not defined yet)
            hamilt_params (dict) parameters dictionary for the required Cheby hamiltonian
            _format: {'type':hamiltonian type, 'Matrix_elems':[mij, ]} 
            _type in ('Sum', 'Multistate', )
            _matrix elements for multistate, see hamilt_elem() function for format
            
        """
        # Chebychev propagator
        if name == 'Cheby':# requires hamiltonian
            # create the propagator subelement of the program
            self._propagation = et.SubElement(self._program, 'propagator', name=name)
            self.def_hamiltonian(hamilt_params)
            # define hamiltonian 
            self._wavefunction.set('states', str(self.states))
            # change wavefunction states based on hamiltonian matrix
        else:
            raise SyntaxError('Propagator type not defined.')
        # others propagators
        try:
            self._program.append( self._wavefunction ) # append wavefunction after the propagation
        except:
            raise SyntaxError('Wavefunction was not properly defined for propa.')    

    propag = typed_property('propagation')
    hamilt = typed_property('hamiltonian')
    
    def def_filterpost(self, filter_list):
        # Define the filterpost operation, must be called after propagation
        filterpost = et.Element('filterpost')
        for dic in filter_list:
            for opes, values in dic.items():
                for keys in values.keys():
                    values[keys] = str(values[keys])
                    # update values to string to satisfy SubElement function
                if opes.startswith('m'):
                    et.SubElement(filterpost.getchildren()[-1], str(opes), values)
                    # m_elements are child of last filter operator
                else:
                    et.SubElement(filterpost, str(opes), values)
        self._program.append(filterpost)
        return filterpost
    
    def filter(self, ftype, params):
        # add filter to calculation
        if ftype == 'filterpost':
            if not isinstance(params, list): params = [params]
            self._filterpost = self.def_filterpost(params)    
            
    
    filterpost = typed_property('filterpost')
        
# %% Name == Main 
if __name__ == "__main__":
    
    dt, steps = 20, 1000
    propag, hamilt = 'Cheby', 'Sum'
    Nef, conv = 20, 1e-9
    name_T, name_V = "GridNablaSq", "GridPotential"
    mass, pot_file = 2000, 'pot_Vg'
    directory = 'efs_g'
    wf_file = 'wfguess'
    file_name='teste_dt_'
    key = 'T'

    nparams = {'dt':1, 'steps':int(1000), 'dir':'efs_g', 'Nef':20, 'conv':1e-11 } 
   
    T00 = {'head':'T', 'name':name_T, 'mass':mass, 'key':'T'}
    V00 = {'head':'V', 'name':name_V, 'file':pot_file}
    m00 = {'head':'m0', 'name':'Sum', 'Opes':[T00, V00]} 
    T11 = {'head':'T', 'ref':'T'}
    V11 = {'head':'V', 'name':name_V, 'file':pot_file}
    m11 = {'head':'m1', 'name':'Sum', 'Opes':[T11, V11]} 
    m22 = {'head':'m2', 'name':'Sum', 'Opes':[T11, V11]} 
    m10 = {'head':'m10', 'name':'GridDipole', 'file':'mu', 'laser':'Et', 'Opes':[]} 

    Hparams = {'type':'Multistate', 'Mels':[m00, m11, m10, m22]} 
    Hsum = {'type':'Sum', 'Opes':[T00, V00, T00]} 
    wf, ef, vib =   [1, ], ['Sig0',], [1, ] # args['wf'], args['ef'], , args['vib'] #
    WFparams = {'type':'Multistate', 'states':'1',
             'file':["MgH/efs_{}/ef_{}".format(ef[i], vib[i]) for i in range(len(ef))], 
             'index':[wf[i] for i in range(len(wf))], 'normalize':True}
    filteropes = [{'expeconly':{'name':'Multistate', 'states':WFparams['states'], 'unity':'False', 'header':"mu{}".format(ind)}, 
                   'm{}'.format(ind):{'name':'GridPotential', 'file':'MgH/mu/mu_Sig0Sig1'}}
                   for ind in [2.1,] ]
    #%%
    prop = InpXML()
    prop.program('propa', nparams, WFparams)
    prop.propagation('Cheby', Hparams)
    prop.filter('filterpost', filteropes)
    prop.hamilt = 'name', 'b'


    prop.show
    # prop.writexml(txt=True)
        

