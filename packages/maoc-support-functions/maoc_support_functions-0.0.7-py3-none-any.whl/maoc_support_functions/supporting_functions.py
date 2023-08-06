#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def MAOC_periodic_table():
    import pandas as pd
    Atom=pd.DataFrame(['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'],columns=['Atom'])
    Z=pd.DataFrame([x for x in range(1,119,1)],columns=['Z'])
    return(pd.concat([Atom,Z],axis=1))


# In[ ]:


def MAOC_partial_charges(file,charge):
    from openbabel import openbabel as ob
    obConversion = ob.OBConversion()
    mol = ob.OBMol()
    path = file
    if not obConversion.ReadFile(mol, file):
        raise FileNotFoundError(f"Could not read molecule {file}")
    mol.SetTotalCharge(charge)
    ob_charge_model=ob.OBChargeModel.FindType('eem2015bn')
    ob_charge_model.ComputeCharges(mol)
    return(ob_charge_model.GetPartialCharges())


# In[ ]:


def MAOC_atom_extraction(file):
    import pandas as pd
    import re
    A=open(file).readlines()
    B=A[2:]
    for qaz in B:
        if qaz=='\n':
            B.remove('\n')
    C=[x.split()[0] for x in B]
    my_dict = {i:C.count(i) for i in C}
    er=pd.DataFrame(my_dict, index=[0])
    B1=[x.split('\n')[0] for x in B if x.split()[0]!='H']
    B2=[x.split('\n')[0] for x in B if x.split()[0]=='H']
    d=[]
    o=0
    for et in B1:
        for y in er:
            for t in range(0,int(er[y])):
                if et.split()[0]==y:
                    d.append(et.split()[0]+str(o)+'    '+et.split()[1]+'    '+et.split()[2]+'    '+et.split()[3])
        o=o+1
    nH=[i for n, i in enumerate(d) if i not in d[:n]]
    ele=[x.split()[0] for x in nH]
    B21=[]
    for i in range(len(B2)):
        B21.append(B2[i].split()[0]+'    '+B2[i].split()[1]+'    '+B2[i].split()[2]+'    '+B2[i].split()[3])
    qwe=nH+B21
    q=[qwe[0]]
    i=0
    for i in range(1,len(qwe)):
        s=q[0]+'; '+qwe[i]
        q=[]
        q.append(s)
        i=i+1
           
    yu=[]
    for p in qwe:
        yu.append(p.split()[0])
    tyu=[]
    for eer in yu:
        tyu.append(re.split('(\d+)',eer)[0])
    at_all=list(set(tyu))
    return(q,yu,at_all)


# In[ ]:


def MAOC_min_ch_max_ch(atom_labels,file,charge):
    import pandas as pd
    tab=pd.concat([pd.DataFrame(atom_labels,columns=['E']),pd.DataFrame(MAOC_partial_charges(file,charge),columns=['G'])],axis=1)
    tab = tab[tab.E != 'H'].dropna()
    tab['G']=tab['G'].round(4)
    ch_min=[x for x in tab['E'].loc[tab['G'] == tab['G'].min()]]
    ch_max=[x for x in tab['E'].loc[tab['G'] == tab['G'].max()]]
    at_min=list(set(d[0] for d in list(ch_min)))
    at_max=list(set(d[0] for d in list(ch_max)))
    return(ch_min,at_min,ch_max,at_max)

