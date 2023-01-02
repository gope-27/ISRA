import pandas as pd

Parametric_df = pd.read_csv('ISRA -21-Dec-2022.csv',header = 1,nrows=5)
values_df = pd.read_csv('ISRA -21-Dec-2022.csv',header = 1, low_memory=False)
pdf = Parametric_df.iloc[:,55:-1]
vdf = values_df.iloc[:,55:-1]
vdf1 = values_df
vdf.drop([0,1,2,3,4],axis=0,inplace=True)
vdf.reset_index(inplace = True, drop = True)
vdf1.drop([0,1,2,3,4],axis=0,inplace=True)
vdf1.reset_index(inplace = True, drop = True)
pdf_columns =list (pdf.columns)
for i in pdf_columns:
    max_value = pdf[i][2]
    min_value = pdf[i][3]
    new_column = str(i+'_flag')
    flag_status = []
    for j in vdf[i]:
        if  j > min_value and j < max_value:
            flag_status.append('Ok')
        else:
            flag_status.append('Not Ok')
    vdf[new_column]=flag_status
flag_df=vdf.iloc[:,-38:-1]
flag_columns=list(flag_df.columns)
flag = []
non_matching = []
for row_count in range(0,flag_df.shape[0]):
    no_column=[]
    yes_count = 0
    for flag_column in flag_columns:
        flag_column1=list(flag_df[flag_column])
        if flag_column1[row_count] == 'Ok':
            yes_count = yes_count+1
        else:
            no_column.append(str(flag_column).replace("_flag", ""))
    if yes_count == len(flag_columns):
        flag.append('Ok')
        non_matching.append('')
    else:
        flag.append('Not Ok')
        non_matching.append((no_column))
vdf1['flag'] =flag
vdf1['non_matching_coln'] = non_matching
vdf1.to_csv('final.csv')
