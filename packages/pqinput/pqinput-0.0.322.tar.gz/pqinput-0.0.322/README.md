# Python package to generate and modify QDng calculations inputs in xml format

### Module:
- `inpxml.py`: **InpXML** 
Class with methods to write and edit *xml* structures designed as input files for quantum chemistry calculations on QDng package. 
Requires *lxml*.


### Example: 

In:
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
    # Initialize
    prop = InpXML()
    prop.program('propa', nparams, WFparams)
    prop.propagation('Cheby', Hparams)
    prop.filter('filterpost', filteropes)
    prop.show

    # Editing
    prop.hamilt = 'name', 'something'
    prop.hamilt = 'm0.0/T', 'name', 'something_new'
    prop.show
     
    # Writing to file
    # prop.writexml(filename='filename', txt=True)

Out:
```xml
<qdng>
  <propa dt="1" steps="1000" dir="efs_g" Nef="20" conv="1e-11">
    <propagator name="Cheby">
      <hamiltonian name="Multistate">
        <m0.0 name="Sum">
          <T name="GridNablaSq" mass="2000" key="T"/>
          <V name="GridPotential" file="pot_Vg"/>
        </m0.0>
        <m1.1 name="Sum">
          <T ref="T"/>
          <V name="GridPotential" file="pot_Vg"/>
        </m1.1>
        <m1.0 name="GridDipole" file="mu" laser="Et"/>
        <m2.2 name="Sum">
          <T ref="T"/>
          <V name="GridPotential" file="pot_Vg"/>
        </m2.2>
      </hamiltonian>
    </propagator>
    <wf name="Multistate" states="3" normalize="true">
      <wf1 file="MgH/efs_Sig0/ef_1"/>
    </wf>
    <filterpost>
      <expeconly name="Multistate" states="1" unity="False" header="mu2.1">
        <m2.1 name="GridPotential" file="MgH/mu/mu_Sig0Sig1"/>
      </expeconly>
    </filterpost>
  </propa>
</qdng>

<qdng>
  <propa dt="1" steps="1000" dir="efs_g" Nef="20" conv="1e-11">
    <propagator name="Cheby">
      <hamiltonian name="something">
        <m0.0 name="Sum">
          <T name="something_new" mass="2000" key="T"/>
          .
          .
          .
```




