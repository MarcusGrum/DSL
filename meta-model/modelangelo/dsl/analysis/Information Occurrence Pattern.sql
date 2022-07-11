-- Load the wanted data.
-- Traverse every information object and check they are involved in more than one conversion. If that is the case, highlight those nodes.
SELECT l.text node_name, n.id focus_nodes1
FROM node_item n
INNER JOIN view_model vm ON (vm.id = n.model)
INNER JOIN label_item l ON (l.node = n.id)
WHERE (
	n.shape = 'dsl.nodes.information_object' AND (
		1 < (SELECT COUNT(DISTINCT n2.id) FROM node_item n2 
			INNER JOIN edge_item e ON (n2.mutant_object = n.mutant_object AND (e.source = n2.id OR e.target = n2.id))
			INNER JOIN node_item nc ON (e.source = nc.id OR e.target = nc.id)
			WHERE (nc.shape = 'dsl.nodes.conversion'))
	)
);