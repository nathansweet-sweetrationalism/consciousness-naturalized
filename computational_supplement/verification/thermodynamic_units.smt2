; Tiny first-order *logical* countermodel, not a physical thermodynamics theorem.
; In particular: local target success does not entail all targets succeed.
(set-logic QF_UF)
(declare-const tested_1 Bool)
(declare-const tested_2 Bool)
(declare-const untested_3 Bool)
(assert tested_1)
(assert tested_2)
(assert (not untested_3))
(check-sat)
(get-model)
