import numpy as np

for NOFT in ['','_wo']:
    file1=f'9{NOFT}_NOFT_xolscore.txt'
    file2=f'9{NOFT}_NOFT_yolscore.txt'
    save_file=f'9{NOFT}_NOFT.txt'
    grey_color=[0.6117,0.6117,0.6117]
    pc1=np.loadtxt(file1,delimiter=',')
    pc2=np.loadtxt(file2,delimiter=',')
    pc=np.concatenate([pc1,pc2])
    r,g,b=pc[:,3],pc[:,4],pc[:,5]
    for i in range(r.shape[0]):
        if r[i]==1 and g[i]==1 and b[i]==1:
            r[i],g[i],b[i]=grey_color
    pc[:,3],pc[:,4],pc[:,5]=r,g,b
    # 0.7098 rgb 灰色 181/255
    # 0.6117 156/255
    np.savetxt(save_file,pc,delimiter=',')