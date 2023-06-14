# DAT Normal Scoring Prototype

# import statements
import pandas as pd
import os

# set file pull
BASEPATH = os.getcwd()
datapath = f"{BASEPATH}/testdat.csv"

# csv to dataframe
datdf = pd.read_csv(datapath)
pd.to_numeric(datdf['C'])
pd.to_numeric(datdf['M'])
pd.to_numeric(datdf['D_B'])

# create copy
datdf2 = datdf.copy()

# create score lists
c_sc = []
m_sc = []
db_sc = []
t_sc = []

# create dictionaries to hold scores, only for db
db_dict = {3:12, 7:10, 15:8, 30:6, 60:4, 90:2, 365:0}


# COLUMN NAMES MAY CHANGE
# Get scores, using c_sc+m_sc+d_sc to determine reliability score
# Provide normal value plus raw score for clarity

for i in range(0,len(datdf)):
    # GET VALUES
    c = datdf.loc[i].at['C']
    m = datdf.loc[i].at['M']
    db = datdf.loc[i].at['D_B']
    
    # GET SCORES
    # c if statements
    if c<5:
        c_sc.append(1)
    elif 5<=c<8:
        c_sc.append(3)
    elif 8<=c<10:
        c_sc.append(5)
    elif 10<=c<12:
        c_sc.append(7)
    elif 12<=c<15:
        c_sc.append(8)
    elif 15<=c<50:
        c_sc.append(9)
    elif 50<=c:
        c_sc.append(10)

    # m if statements
    if m<12:
        m_sc.append(1)
    elif 12<=m<16:
        m_sc.append(2)
    elif 16<=m<20:
        m_sc.append(3)
    elif 20<=m<25:
        m_sc.append(4)
    elif 25<=m<30:
        m_sc.append(5)
    elif 30<=m<40:
        m_sc.append(6)
    elif 40<=m<50:
        m_sc.append(7)
    elif 50<=m<75:
        m_sc.append(8)
    elif 75<=m<100:
        m_sc.append(9)
    elif 100<=m:
        m_sc.append(10)

    if db in db_dict:
        db_sc.append(db_dict.get(db))
    
    # SUM SCORES
    t_sc.append(c_sc[i]+m_sc[i]+db_sc[i])

# ADD TO DATA FRAME 2, COPY TO CREATE DATAFRAME 3
datdf2['TSC']=t_sc
datdf2['MSC']=m_sc
datdf2['DB_SC']=db_sc
datdf2['T_SC']=t_sc

datdf3 = datdf2.copy()

# Calculate norms for total scores
# Get min max values
tmax = datdf2['T_SC'].max()
tmin = datdf2['T_SC'].min()

# create score list
tn_sc = []

# calculate norms and add to list
for i in range(0,len(datdf2)):
    ts = datdf2.loc[i,'T_SC']
    tsn = (ts-tmin)/(tmax-tmin)
    tn_sc.append(tsn)

#add scores to df
datdf3['TN']=tn_sc
print(datdf3)
# move df to csv
datdf3.to_csv(BASEPATH+'/testresults.csv',index=False)