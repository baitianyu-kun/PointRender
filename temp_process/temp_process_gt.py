import numpy as np

b=0
mask_src=np.load('9_wo_NOFT_masksrc.npy')[0]
mask_tgt=np.load('9_wo_NOFT_masktgt.npy')[0]

src=np.load('9_wo_NOFT_trans_src.npy')[0]
tgt=np.load('9_wo_NOFT_tgt.npy')[0]
src_nonoverlap=src[mask_src==0,:]
# （numpts, 6）,（xyz and 1,1,1），(white color)
src_nonoverlap_color=np.concatenate([src_nonoverlap,\
    np.ones(src_nonoverlap.shape[0]).reshape(src_nonoverlap.shape[0],1),
    np.ones(src_nonoverlap.shape[0]).reshape(src_nonoverlap.shape[0],1),
    np.ones(src_nonoverlap.shape[0]).reshape(src_nonoverlap.shape[0],1),],axis=1)
tgt_nonoverlap=tgt[mask_tgt==0,:]
overlap=tgt[mask_tgt==1,:]
# （numpts, 6）,（xyz and 1,1,1），(white color)
tgt_nonoverlap_color=np.concatenate([tgt_nonoverlap,\
    np.ones(tgt_nonoverlap.shape[0]).reshape(tgt_nonoverlap.shape[0],1),
    np.ones(tgt_nonoverlap.shape[0]).reshape(tgt_nonoverlap.shape[0],1),
    np.ones(tgt_nonoverlap.shape[0]).reshape(tgt_nonoverlap.shape[0],1),],axis=1)

overlap_color=np.concatenate([overlap,\
    np.zeros(overlap.shape[0]).reshape(overlap.shape[0],1),
    np.zeros(overlap.shape[0]).reshape(overlap.shape[0],1),
    np.zeros(overlap.shape[0]).reshape(overlap.shape[0],1),],axis=1)

pc=np.concatenate([src_nonoverlap_color,tgt_nonoverlap_color,overlap_color])

r,g,b=pc[:,3],pc[:,4],pc[:,5]
grey_color=[0.6117,0.6117,0.6117]
red_color=[0.545,0,0]
for i in range(r.shape[0]):
    if r[i]==1 and g[i]==1 and b[i]==1:
        r[i],g[i],b[i]=grey_color
    elif r[i]==0 and g[i]==0 and b[i]==0:
        r[i],g[i],b[i]=red_color
pc[:,3],pc[:,4],pc[:,5]=r,g,b
np.savetxt('NOFT_gt.txt',pc,delimiter=',')

