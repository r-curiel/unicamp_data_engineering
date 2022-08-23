-- SELECT OLAP
SELECT TOP 1
	A.ID_ATENDIMENTO
	, PRI.PRIORIDADE
	, TP.TIPO
	, PAC.NOME 'PACIENTE'
	, PAC.SEXO
	, TEM2.DATA 'NASCIMENTO'
	, PAC.EMAIL
	, CIT.CIDADE 'CIDADE_PAC'
	, DEN.NOME 'DENTISTA'
	, DEN.SEXO
	, DEN.CREDENCIAL
	, ESP.ESPECIALIDADE
	, TEM.DATA 'DATA_CONSULT'
	, A.HORA_INICIO
	, A.HORA_FIM
	, A.FATURA
FROM [fato].[OLAP_ATENDIMENTO] A
LEFT JOIN [dim].[OLAP_PRIORIDADE] PRI ON A.SK_PRIORIDADE = PRI.SK_PRIORIDADE
LEFT JOIN [dim].[OLAP_TIPO] TP ON A.SK_TIPO = TP.SK_TIPO
LEFT JOIN [dim].[OLAP_PACIENTE] PAC ON A.SK_PACIENTE = PAC.SK_PACIENTE
LEFT JOIN [dim].[OLAP_CIDADE] CIT ON PAC.SK_CIDADE = CIT.SK_CIDADE
LEFT JOIN [dim].[OLAP_DENTISTA] DEN ON A.SK_DENTISTA = DEN.SK_DENTISTA
LEFT JOIN [dim].[OLAP_ESPECIALIDADE] ESP ON DEN.SK_ESPECIALIDADE = ESP.SK_ESPECIALIDADE
LEFT JOIN [dim].[OLAP_TEMPO] TEM ON A.DATA = TEM.SK_DATA
LEFT JOIN [dim].[OLAP_TEMPO] TEM2 ON PAC.NASCIMENTO = TEM2.SK_DATA
ORDER BY NEWID() -- ORDENA ALEATORIAMENTE

-- SELECT OLTP
SELECT TOP 1
	A.[ID_ATENDIMENTO]
	, B.[PRIORIDADE]
	, C.[TIPO]
	, A.PACIENTE
	, D.SEXO
	, D.NASCIMENTO
	, D.EMAIL
	, D.CIDADE 'CIDADE_PAC'
	, E.NOME 'DENTISTA'
	, E.SEXO
	, E.CREDENCIAL
	, E.ESPECIALIDADE
	, F.DATA 'DATA_CONSULT'
	, F.HORA_INICIO
	, F.HORA_FIM
	, A.FATURA
FROM [tmp].[OLTP_ATENDIMENTO] A
LEFT JOIN [tmp].[OLTP_PRIORIDAD] B ON A.ID_ATENDIMENTO = B.ID_ATENDIMENTO
LEFT JOIN [tmp].[OLTP_TIP] C ON A.ID_ATENDIMENTO = C.ID_ATENDIMENTO
LEFT JOIN [tmp].[OLTP_PACIENTE] D ON A.PACIENTE = D.NOME
LEFT JOIN [tmp].[OLTP_DENTISTA] E ON A.DENTISTA = E.NOME
LEFT JOIN [tmp].[OLTP_TEMPO] F ON A.ID_ATENDIMENTO = F.ID_ATENDIMENTO
ORDER BY NEWID() -- ORDENA ALEATORIAMENTE