from ICD_9_Ontology import ICD_9_Ontology
a = ICD_9_Ontology()


b = a.get_concept_by_cid('042')
print(b.get())
print(b.Is_fine_grained())

lis1 = b.get_descendants()
for concept in lis1:
    print(concept.get())

lis2 = b.get_all_ancestor()
for concept in lis2:
    print(concept.get())
