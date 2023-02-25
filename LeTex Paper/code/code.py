[NDSet, population] = myAlgorithm.run()  
    NDSet.save()  
    Variable = []
    for i in range(len(NDSet.Phen.tolist())):
        v = NDSet.Phen.tolist()[i]
        Variable.append(v)
    NDSet.Phen = np.array(Variable)
    NDSet.sizes = len(Variable)
    problem.aimFunc(NDSet)
    df1 = pd.DataFrame(NDSet.Phen)
    df2 = pd.DataFrame(NDSet.ObjV)
    obj_item = np.array(df2).tolist()
    obj = []
    for item in obj_item:
        obj.append(0.5*item[0]+0.5*item[1])
    knee_idx = obj.index(max(obj))
    print(f'Knee：f1:{obj_item[knee_idx][0]}, f2:{obj_item[knee_idx][1]}')
    X = np.array(df1.iloc[knee_idx,:]).tolist()
    new = sorted(X)
    new_X = []
    for item in X:
        new_X.append(new.index(item)+1)
    print(new_X)
    print(caltime(new_X))
    df1.to_csv('Variable.csv', header=None, index=None)
    df2.to_csv('Objective.csv', header=None, index=None)

def aimFunc(self, pop):  # 目标函数
    Vars = pop.Phen  # 得到决策变量矩阵
    Vars = np.array(Vars, dtype=float)
    popsize = Vars.shape[0]
    F1 = np.array([float("Inf")] * popsize).reshape(popsize, 1)
    F2 = np.array([float("Inf")] * popsize).reshape(popsize, 1)
    for i in range(popsize):
        X = []
        for j in range(34):
            x = Vars[i, [j]][0]
            X.append(x)
        new = sorted(X)
        new_X = []
        for item in X:
            new_X.append(new.index(item))
     pop.Phen = np.hstack((x1,x2,x3,x4,x5,x6,x7))
        # 时间
        f1 = 0
        w = 0
        for k in range(17):
            if k == 0:
                f1 += 1
            else:
                for j in range(1, k):
                    w += weight.iloc[new_X[j], new_X[k]]
                    w = w / k
                    f1 += ((1 - w) * Time.iloc[new_X[j], new_X[k]]-new
        F1[i, 0] = f1
        F2[i, 0] = f2
