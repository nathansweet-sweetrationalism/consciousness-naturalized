; Falsifies the universal implication that intersection with two sets is
; necessarily a PROPER subset of the initial set.
(set-logic QF_UF)
(declare-const in_r_0 Bool)
(declare-const in_r_1 Bool)
(declare-const in_theta_0 Bool)
(declare-const in_theta_1 Bool)
(declare-const in_c_0 Bool)
(declare-const in_c_1 Bool)
; Every element belongs to all three subsets: equality is possible.
(assert in_r_0)
(assert in_r_1)
(assert in_theta_0)
(assert in_theta_1)
(assert in_c_0)
(assert in_c_1)
(check-sat)
(get-model)
