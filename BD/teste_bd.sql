SELECT * from Agenda;
INSERT INTO Agenda (data,horario,descricao) VALUES ("16/07","!3:30","Treino");
UPDATE Agenda
SET descricao = "eu"
WHERE id = 3;
DELETE FROM agenda WHERE id = 2;
