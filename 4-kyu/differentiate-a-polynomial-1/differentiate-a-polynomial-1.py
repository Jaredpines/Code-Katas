from decimal import Decimal, getcontext
import re
​
getcontext().prec = 50
​
def differentiate_term_exact(term):
    term = term.strip()
    if not term:
        return "0"
    
    if 'x^' in term:
        coeff_part, coeff_exp = term.split('x^')
        if coeff_part == '' or coeff_part == '+': coeff = 1
        elif coeff_part == '-': coeff = -1
        else: coeff = int(coeff_part)
        
        exp = int(coeff_exp)
        new_coeff = coeff * exp
        new_exp = exp - 1
        
        return f"Decimal('{new_coeff}') * (Decimal(x) ** {new_exp})"
    
    elif 'x' in term:
        coeff_part = term.replace('x', '')
        if coeff_part == '' or coeff_part == '+': return "Decimal('1')"
        if coeff_part == '-': return "Decimal('-1')"
        return f"Decimal('{coeff_part}')"
    
    else:
        return "Decimal('0')"
​
def differentiate(equation, point):
    cleaned = equation.replace('-', ' -').replace('+', ' +')
    terms = cleaned.split()
    
    derivative_terms = [differentiate_term_exact(t) for t in terms]
    derivative_expr = " + ".join(derivative_terms)
    
    math_string = derivative_expr.replace("x", f"'{point}'")
    
    import builtins
    local_env = {"Decimal": Decimal}
    final_answer = builtins.eval(math_string, {}, local_env)
    
    return int(final_answer)