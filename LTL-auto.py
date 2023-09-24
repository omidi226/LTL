import minizinc
# Create model
    model = minizinc(["LTL.mzn"])
    m = Model()
    m.add_string(
    """
    int:n;
    array[0..n] of var 0..1:q;
    
    predicate P ( array[0..n] of var 0..1:q)=
    q[0] =1 ;
    output ["\\(predicate P ( array[0..n] of var 0..1:q)=
    q[0] =1 ;)"];
    """
    )