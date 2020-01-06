# This sample generates a single random bit.
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE

p = Program()
ro = p.declare('ro', 'BIT', 0)
p += H(0)
p += MEASURE(0, ro[0])

print(p)

qc = get_qc('1q-qvm') 
executable = qc.compile(p)
result = qc.run(executable)
print(result)