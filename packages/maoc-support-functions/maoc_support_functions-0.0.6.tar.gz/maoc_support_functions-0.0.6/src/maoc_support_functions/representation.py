#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#The code that generates the MAOC representation
def MAOC(PATH=None, basis_set='sto-3g',charge=0,nr_pca=None,spin=None,pre_orth_AO='ANO',pca_explanation=True):
    from pyscf import scf,gto,lo
    import glob
    import pandas as pd
    import re
    import numpy as np
    from maoc_support_functions.supporting_functions import MAOC_atom_extraction
    from maoc_support_functions.supporting_functions import MAOC_min_ch_max_ch
    from maoc_support_functions.supporting_functions import MAOC_partial_charges
    from maoc_support_functions.supporting_functions import MAOC_periodic_table
    from natsort import natsorted
    from sklearn.decomposition import PCA
    from openbabel import openbabel as ob
    
    maoc_pca=[] # A list used to store PCX-MAOC arrays. Users can simply transform the [1,X] array into [N,X/N] and use the non-flattened representation. 
    
    maoc=[] # A list having the MAOC array. If the flattened version is used, each element is represented by a [1, M] array, whereas the extent of the array for the non-flatten version is [sqr(M),sqr(M)].
    
    pca_exp=[] # A listing of the MO contribution to the N principal components.
    
    for file in natsorted(glob.glob(PATH)): # This code sorts the PATH files in a natural order (0,1,2,...) rather than by their first number (0,1,10,100,2,20).
        
        atom_label_coordinates,atom_labels,atom_type=MAOC_atom_extraction(file) # Playing with the XYZ file, getting the number, type, and locations of the atoms, and marking them.
        min_ch,min_ch_at,max_ch,max_ch_at=MAOC_min_ch_max_ch(atom_labels,file,charge) # Getting the partial charges of the atoms and picking the ones with the lowest and the greatest charges.
        
        mol1 = gto.Mole() # Creating the molecule.
        mol1.atom = atom_label_coordinates[0] # The specification of atomic coordinates.
        mol1.charge=charge # Specifying the molecule's charge. Be careful!!! Two compounds with the same geometry but a distinct number of electrons have the same mol1.charge (charge invariance).
        if spin != None:
            mol1.spin=spin
        else:
            mol1.spin=abs((mol1.nelectron) % 2) # Specifying the molecule's spin multiplicity. Be careful!!! Two compounds with the same geometry but a distinct number of spin have the same mol1.spin (spin invariance).
        # The user may question how we were able to generate a charge variant representation when mol1.charge and mol1.spin are insensitive to the charge and spin of compounds. This is made using the below technique:
        
        if mol1.charge==0:
            dic={x:basis_set for x in atom_type} # For neutral compounds, every atom has its own basis set (e.g., C has its own basis set).
        elif mol1.charge<0: # In the case of anionic compounds, the code modifies the basis set of the atom with the greatest partial charge to that of the atom with Z+|charge|.
            dic={x:basis_set for x in atom_type}
            for i in max_ch:
                dic[i]=gto.basis.load(basis_set,MAOC_periodic_table()['Atom'][MAOC_periodic_table().index[MAOC_periodic_table()['Z'] == (int(MAOC_periodic_table()[MAOC_periodic_table()['Atom']==re.split('(\d+)',(max_ch_at[0]))[0]]['Z'])-mol1.charge)].tolist()[0]])
        elif mol1.charge>0: # In the case of cationic compounds, the code modifies the basis set of the atom with the smallest partial charge to that of the atom with Z-|charge|.
            dic={x:basis_set for x in atom_type}
            for i in min_ch:
                dic[i]=gto.basis.load(basis_set,MAOC_periodic_table()['Atom'][MAOC_periodic_table().index[MAOC_periodic_table()['Z'] == (int(MAOC_periodic_table()[MAOC_periodic_table()['Atom']==re.split('(\d+)',(min_ch_at[0]))[0]]['Z'])-mol1.charge)].tolist()[0]])
        mol1.basis=dic # Using the basis set you got from the previous steps.
        mol1.build()
        
        core=pd.DataFrame(lo.orth_ao(mol1,method='meta_lowdin', pre_orth_ao=pre_orth_AO)) # MAOC representation generation. For more information, please visit https://pyscf.org/pyscf_api_docs/pyscf.lo.html.

        
        for i in range(0,mol1.nelec[1],1):
            core[i]=core[i]*2 # A coefficient that remains constant and is multiplied by the doubly occupied MOs' coefficients.
        for u in range(mol1.nelec[1],(mol1.nelec[1]+(mol1.nelec[0]-mol1.nelec[1])),1):
            core[u]=core[u]*1 # A coefficient that remains constant and is multiplied by the singly occupied MOs' coefficients.
        for e in range((mol1.nelec[1]+(mol1.nelec[0]-mol1.nelec[1])),core.shape[0],1):
            core[e]=core[e]*0.5 # A coefficient that remains constant and is multiplied by the virtual MOs' coefficients.
    
        # Sorting the MAOC array and making it permutationally invariant.
        
        for col in core:
            core[col] = core[col].sort_values(ignore_index=True,ascending=False) # Sorting each column's elements.
        sqr_core = core.sort_values(by =0, axis=1,ascending=False) # Sorting by the values of the first row in descending order.
        sqr_core1=abs(pd.DataFrame(sqr_core)).round(4) # Making each element of the matrix a positive number with four significant digits (saving computation time and storage space during generation). 
        
        # Computing the PCX-MAOC representation:
        if nr_pca !=None:
            pca = PCA(n_components=nr_pca) # Specification of the number of components.
            maoc_pca.append(np.array(pca.fit_transform(sqr_core1)).T.flatten()) # Generating the PCX-MAOC flattened variant. For the non-flatten version, transform [1,X] into the array [N,X/N].
            exp_pca=pca.components_ # Determine the overall MO (not sorted) contribution in the PCX. 
            Q=pd.concat([pd.DataFrame(range(0,pd.DataFrame(exp_pca).T[0].size,1),columns=['Orbital_no']),pd.DataFrame(exp_pca).T],axis=1)
            q=[]
            for i in range(0,len(Q[0]),1):
                if int(mol1.nelectron/2)-i-charge >0:
                    q.append('HOMO-'+str(int(mol1.nelectron/2)-i-charge)) # Get the contribution from MO1 until HOMO-1.
                elif int(mol1.nelectron/2)-i-charge ==0:
                    q.append('HOMO') # Get the HOMO contribution.
                elif int(mol1.nelectron/2)-i-charge ==-1:
                    q.append('LUMO') # Get the LUMO contribution.
                elif int(mol1.nelectron/2)-i-charge <0:
                    q.append('LUMO+'+str(-int(mol1.nelectron/2)+i-1-charge)) # Get the contribution from LUMO+1 until MO_last.
            pca_exp.append(pd.concat([Q,pd.DataFrame(q,columns=['Type'])],axis=1))
        else: 
            maoc.append(sqr_core1.to_numpy()) # Generating the MAOC flattened version. For the non-flattening version, transform [1,M] into the array [sqr(M),sqr(M)].
    if nr_pca !=None and pca_explanation == True:
        return maoc_pca, pca_exp
    elif nr_pca !=None and pca_explanation == False:
        return maoc_pca
    else:
        return maoc

