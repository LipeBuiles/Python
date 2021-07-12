def facturarTotal(orden:list):
    ord = []
    tus = ()
    my_list=()
    final_list=[]
    for ord in orden:
        num_pedido = list( filter(lambda element: (type(element))==int, ord))
        num_pedido = int(num_pedido[0])
        aux = 0
    
        for tus in ord:
            if type(tus)!=int:
                mult = tus[1]*tus[2]
                aux = mult+aux
        
        if aux<1000000:
            square = lambda x: x + 30000
            aux = square(aux)
            my_list=(num_pedido,aux)
        else:
            my_list=[num_pedido,aux]

        final_list.append(my_list)
    print(final_list)

orden = [[1,("5464",1,30000),("8274",2,42000),("9744",3,150000)], [2,("7733",3,80000),("88112",10,45000),("5464",2,30000),("9744",9,150000)], [3,("88112",25,45000)],
[4,("5464",9,30000),("9744",20,150000)],
[5,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]

facturarTotal(orden)