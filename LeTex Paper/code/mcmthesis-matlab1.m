function [Q]=AHP(B) [n,m]=size(B);
for i=1:n
    for j=1:n
        if B(i,j)*B(j,i)~=1   
        fprintf('i=%d,j=%d,B(i,j)=%d,B(j,i)=%d\n',i,j,B(i,j),B(j,i))  
        end  
    end
end
[V,D]=eig(B);tz=max(D);tzz=max(tz);c1=find(D(1,:)==max(tz));Q=quan;
CI=(tzz-n)/(n-1);
RI=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49,1.52,1.54,1.56,1.58,1.59];
