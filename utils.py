def set_hyperlink(link):
    '''
    Creates clickable hyperlink out of exisiting link of type string.
    '''
    return f'<a href="{link}" target="_blank">{link}</a>'

def return_clean_data(data_file):
    '''
    Input: the data file's name ("hsp_data.xlsx"). 
    Output: ready to use df.
    '''

    from IPython.display import display, HTML
    import pandas as pd
    pd.set_option('display.max_columns', None)

    data = pd.read_excel(data_file)

    # remap findings titles to category-specific titles
    titles_map = {'U-fiber/Juxtacortical involvement':'U-Fiber/Juxtacortical Involvement',
                'Cortical involvement/Subcortical Lesions':'Cortical Involvement/Subcortical Lesions',
                'Telltale grey matter involvement':'Telltale Grey Matter Involvement',
                'Forceps major':"Periventricular Involvement:Forceps Major",
                'Forceps minor':"Periventricular Involvement:Forceps Minor",
                'Other':"Periventricular Involvement:Other",
                'Rostrum':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Rostrum",
                'Genu':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Genu",
                'Body':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Body",
                'Isthmus':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Isthmus",
                'Splenium':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Splenium",
                'Other.1':"Subcortical Structures:Corpus Callosum Involvement (Atrophy):Other",
                'Cerebellar ':"Subcortical Structures:Posterior Fossa Involvement:Cerebellar",
                'Brainstem':"Subcortical Structures:Posterior Fossa Involvement:Brainstem",
                'Spinal cord atrophy':"Spinal Cord Involvement:Spinal Cord Atrophy",
                'Abnormal signal/white matter tract':"Spinal Cord Involvement:Abnormal Signal/White Matter Tract",
                'Ventriculomegaly vs hydrocephalus':'Ventriculomegaly vs Hydrocephalus',
                'Other.2':'Other'}
    data = data.rename(columns=titles_map)

    # standarize unique values in each column (MRI findings)
    data['Diffuse or Multifocal'] = data['Diffuse or Multifocal'].replace({'D,M':'D, M'})
    data['Periventricular Involvement:Forceps Major'] = data['Periventricular Involvement:Forceps Major'].replace('x','present')
    data['Periventricular Involvement:Forceps Minor'] = data['Periventricular Involvement:Forceps Minor'].replace('x','present')
    data['Periventricular Involvement:Other'] = data['Periventricular Involvement:Other'].replace('x','present')
    data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Rostrum'] = data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Rostrum'].replace('x','present')
    data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Genu'] = data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Genu'].replace('x','present')
    data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Body'] = data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Body'].replace({'x':'present', 'indenture, x ':'indenture, present '})
    data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Isthmus'] = data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Isthmus'].replace('x','present')
    data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Splenium'] = data['Subcortical Structures:Corpus Callosum Involvement (Atrophy):Splenium'].replace('x','present')
    data['Subcortical Structures:Posterior Fossa Involvement:Cerebellar'] = data['Subcortical Structures:Posterior Fossa Involvement:Cerebellar'].replace('x','present')
    data['Spinal Cord Involvement:Spinal Cord Atrophy'] = data['Spinal Cord Involvement:Spinal Cord Atrophy'].replace('x','present')

    # create hyperlinks
    #data['Genome Browser'] = data['Genome Browser'].apply(set_hyperlink)
    #data['Articles'] = data['Articles'].apply(set_hyperlink)
    #data['Articles with MR Images'] = data['Articles with MR Images'].apply(set_hyperlink)
    #data['OMIM'] = data['OMIM'].apply(set_hyperlink)
    #data['Oprha link'] = data['Oprha link'].apply(set_hyperlink)

    # fix missing values values
    data = data.fillna('')

    # Render DataFrame as HTML
    #html = data.to_html(escape=False)

    # Display HTML content
    # display(HTML(html))

    return data

def check_multiple_dimensions(main_category_title):
    '''
    Return True if category has subcategories and False otherwise.
    '''
    findings_categorized = {
 'Diffuse or Multifocal':'Diffuse or Multifocal', # 1-dimensional category
 'Symmetric':'Symmetric',
 'Frontal vs Posterior Predominance':'Frontal vs Posterior Predominance',
 'Telltale Grey Matter Involvement':'Telltale Grey Matter Involvement',
 'Cortical Involvement/Subcortical Lesions':'Cortical Involvement/Subcortical Lesions',
 'U-Fiber/Juxtacortical Involvement':'U-Fiber/Juxtacortical Involvement',
 'Ventriculomegaly vs Hydrocephalus':'Ventriculomegaly vs Hydrocephalus',

 'Spinal Cord Involvement':{ # 2-dimensional category
                            'Spinal Cord Atrophy':'Spinal Cord Atrophy',
                            'Abnormal Signal/White Matter Tract':'Abnormal Signal/White Matter Tract'},
 'Periventricular Involvement':{
                                'Forceps Major':'Forceps Major',
                                'Forceps Minor':'Forceps Minor',
                                'Other':'Other'},

 'Subcortical Structures':{# 3-dimensional category
                           'Corpus Callosum Involvement (Atrophy)':{
                                                                    'Rostrum':'Rostrum',
                                                                    'Genu':'Genu',
                                                                    'Body':'Body',
                                                                    'Isthmus':'Isthmus',
                                                                    'Splenium':'Splenium',
                                                                    'Other':'Other'},
                           'Posterior Fossa Involvement':{
                                                          'Cerebellar':'Cerebellar',
                                                          'Brainstem':'Brainstem'}}
}
    return type(findings_categorized[main_category_title])==dict


findings_categorized = {
 'Diffuse or Multifocal':'Diffuse or Multifocal', # 1-dimensional category
 'Symmetric':'Symmetric',
 'Frontal vs Posterior Predominance':'Frontal vs Posterior Predominance',
 'Telltale Grey Matter Involvement':'Telltale Grey Matter Involvement',
 'Cortical Involvement/Subcortical Lesions':'Cortical Involvement/Subcortical Lesions',
 'U-Fiber/Juxtacortical Involvement':'U-Fiber/Juxtacortical Involvement',
 'Ventriculomegaly vs Hydrocephalus':'Ventriculomegaly vs Hydrocephalus',

 'Spinal Cord Involvement':{'Spinal Cord Atrophy':'Spinal Cord Atrophy', # 2-dimensional category
                            'Abnormal Signal/White Matter Tract':'Abnormal Signal/White Matter Tract'},
 'Periventricular Involvement':{'Forceps Major':'Forceps Major',
                                'Forceps Minor':'Forceps Minor',
                                'Other':'Other'},

 'Subcortical Structures':{'Corpus Callosum Involvement (Atrophy)':{'Rostrum':'Rostrum', # 3-dimensional category
                                                                    'Genu':'Genu',
                                                                    'Body':'Body',
                                                                    'Isthmus':'Isthmus',
                                                                    'Splenium':'Splenium',
                                                                    'Other':'Other'},
                           'Posterior Fossa Involvement':{'Cerebellar':'Cerebellar',
                                                          'Brainstem':'Brainstem'}}
}