import ProjectClass as p


project1 = p.Project(1001,'SAP Implementation',25,'09/30/2022')
project2 = p.Project(1002,'Migration to CRM',10,'06/30/2022')

projectDict = {project1.get_projID(): project1.get_dueDate(), project2.get_projID(): project2.get_dueDate()}

print(projectDict)