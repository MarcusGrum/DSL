---- DSL
INSERT INTO meta_model (id, name, author, version) VALUES ('dsl', 'DSL', 'System', 26);

-- DSL.nodes
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.activity_border', 'dsl', 'Activity Border', 'dsl/nodes/activity_border', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.and', 'dsl', 'And', 'dsl/nodes/and', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.conversion', 'dsl', 'Activity', 'dsl/nodes/conversion', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.information_object', 'dsl', 'Explicit Knowledge Object', 'dsl/nodes/information_object', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.information_system', 'dsl', 'Information System', 'dsl/nodes/information_system', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.knowledge_border', 'dsl', 'Knowledge Border', 'dsl/nodes/knowledge_border', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.knowledge_object', 'dsl', 'Tacit Knowledge Object', 'dsl/nodes/knowledge_object', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.mixed_knowledge_object', 'dsl', 'Mixed Knowledge Object', 'dsl/nodes/mixed_knowledge_object', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.or', 'dsl', 'Or', 'dsl/nodes/or', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.person', 'dsl', 'Person', 'dsl/nodes/person', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.process_border', 'dsl', 'Process Border', 'dsl/nodes/process_border', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.role', 'dsl', 'Role', 'dsl/nodes/role', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.task', 'dsl', 'Task', 'dsl/nodes/task', 'n');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.nodes.xor', 'dsl', 'Xor', 'dsl/nodes/xor', 'n');
-- DSL.edges
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.aggregation', 'dsl', 'Aggregation', 'dsl/edges/aggregation', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.combination', 'dsl', 'Combination', 'dsl/edges/combination', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.control_flow', 'dsl', 'Control Flow', 'dsl/edges/control_flow', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.externalization', 'dsl', 'Externalization', 'dsl/edges/externalization', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.internalization', 'dsl', 'Internalization', 'dsl/edges/internalization', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.membership', 'dsl', 'Membership', 'dsl/edges/membership', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.socialization', 'dsl', 'Socialization', 'dsl/edges/socialization', 'e');
INSERT INTO graphic (id, meta_model, shape, path, type) VALUES ('dsl.edges.undefined_conversion', 'dsl', 'Undefined Conversion', 'dsl/edges/undefined_conversion', 'e');

--- DSL.Activity View
INSERT INTO view (id, meta_model, name, author, version, global) VALUES ('DSL.activity_view', 'dsl', 'Activity View', 'Marcus Grum', 1, true);
-- DSL.Activity View.nodes
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.activity_border', 'DSL.activity_view', 'dsl.nodes.activity_border', true, 0, 4);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.conversion', 'DSL.activity_view', 'dsl.nodes.conversion', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.information_object', 'DSL.activity_view', 'dsl.nodes.information_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:nodes.information_system', 'DSL.activity_view', 'dsl.nodes.information_system', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.knowledge_object', 'DSL.activity_view', 'dsl.nodes.knowledge_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.mixed_knowledge_object', 'DSL.activity_view', 'dsl.nodes.mixed_knowledge_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.nodes.person', 'DSL.activity_view', 'dsl.nodes.person', true, 2, 2);
-- DSL.Activity View.edges
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.combination', 'DSL.activity_view', 'dsl.edges.combination', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.externalization', 'DSL.activity_view', 'dsl.edges.externalization', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.internalization', 'DSL.activity_view', 'dsl.edges.internalization', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.membership', 'DSL.activity_view', 'dsl.edges.membership', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.socialization', 'DSL.activity_view', 'dsl.edges.socialization', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.activity_view:0.edges.undefined_conversion', 'DSL.activity_view', 'dsl.edges.undefined_conversion', false, 2, 2);

--- DSL.Knowledge Overview
INSERT INTO view (id, meta_model, name, author, version, global) VALUES ('DSL.knowledge_overview', 'dsl', 'Knowledge Overview', 'Marcus Grum', 1, true);
-- DSL.Knowledge Overview.nodes
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.information_object', 'DSL.knowledge_overview', 'dsl.nodes.information_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.information_system', 'DSL.knowledge_overview', 'dsl.nodes.information_system', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.knowledge_border', 'DSL.knowledge_overview', 'dsl.nodes.knowledge_border', true, 0, 4);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.knowledge_object', 'DSL.knowledge_overview', 'dsl.nodes.knowledge_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.mixed_knowledge_object', 'DSL.knowledge_overview', 'dsl.nodes.mixed_knowledge_object', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:nodes.person', 'DSL.knowledge_overview', 'dsl.nodes.person', true, 2, 2);
-- DSL.Knowledge Overview.edges
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:edges.aggregation', 'DSL.knowledge_overview', 'dsl.edges.aggregation', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.knowledge_overview:edges.membership', 'DSL.knowledge_overview', 'dsl.edges.membership', false, 2, 2);

--- DSL.Process View
INSERT INTO view (id, meta_model, name, author, version, global) VALUES ('DSL.process_view', 'dsl', 'Process View', 'Marcus Grum', 1, true);
-- DSL.Process View.nodes
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.and', 'DSL.process_view', 'dsl.nodes.and', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.information_system', 'DSL.process_view', 'dsl.nodes.information_system', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.or', 'DSL.process_view', 'dsl.nodes.or', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.process_border', 'DSL.process_view', 'dsl.nodes.process_border', true, 0, 4);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.role', 'DSL.process_view', 'dsl.nodes.role', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.task', 'DSL.process_view', 'dsl.nodes.task', true, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.nodes.xor', 'DSL.process_view', 'dsl.nodes.xor', false, 2, 2);
-- DSL.Process View.edges
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.edges.control_flow', 'DSL.process_view', 'dsl.edges.control_flow', false, 2, 2);
INSERT INTO graphics_to_view (id, view, graphic, labeled, h_align, v_align) VALUES ('DSL.process_view:0.edges.membership', 'DSL.process_view', 'dsl.edges.membership', false, 2, 2);

