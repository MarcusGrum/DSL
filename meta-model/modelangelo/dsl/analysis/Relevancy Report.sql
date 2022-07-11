-- Setup the following queries and map the data fields (data table columns) to the output fields by using special column labels.
SELECT
	'setup' query_type, 'Name' th1, 'INT' th2, 'EXT' th3, 'SOC' th4, 'COMB' th5, 'UNDEF' th6,
	'node_name' td1, 'ints' td2, 'exts' td3, 'socs' td4, 'combs' td5, 'undefs' td6,
	'ints' sum2, 'exts' sum3, 'socs' sum4, 'combs' sum5, 'undefs' sum6,
	'Relevancy Report' dia_title, 'Conversion Types' dia_x_label, 'Number of Occurrence' dia_y_label
FROM node_item
LIMIT 1;

-- Load the wanted data.
-- Traverse every conversion (atomic, complex, and abstract) and count the incoming and outgoing externalizations, internalization, socializations, combinations, and undefined conversions.
SELECT l.text node_name,
	(SELECT COUNT(*) FROM edge_item e
		WHERE (e.shape = 'dsl.edges.internalization'
			AND (e.source = n.id OR e.target = n.id))) ints,
	(SELECT COUNT(*) FROM edge_item e
		WHERE (e.shape = 'dsl.edges.externalization'
			AND (e.source = n.id OR e.target = n.id))) exts,
	(SELECT COUNT(*) FROM edge_item e
		WHERE (e.shape = 'dsl.edges.socialization'
			AND (e.source = n.id OR e.target = n.id))) socs,
	(SELECT COUNT(*) FROM edge_item e
		WHERE (e.shape = 'dsl.edges.combination'
			AND (e.source = n.id OR e.target = n.id))) combs,
	(SELECT COUNT(*) FROM edge_item e
		WHERE (e.shape = 'dsl.edges.undefined_conversion'
			AND (e.source = n.id OR e.target = n.id))) undefs
FROM node_item n
INNER JOIN view_model vm ON (vm.id = n.model)
INNER JOIN label_item l ON (l.node = n.id)
WHERE (
	n.shape = 'dsl.nodes.conversion' AND (
		0 < (SELECT COUNT(*) FROM edge_item WHERE target = n.id)
		AND 0 < (SELECT COUNT(*) FROM edge_item WHERE source = n.id)
	)
);

-- Flush the loaded data to the output.
SELECT 'flush' query_type
FROM node_item
LIMIT 1;

-- Finally show the analysis' results.
SELECT 'show' query_type
FROM node_item
LIMIT 1;