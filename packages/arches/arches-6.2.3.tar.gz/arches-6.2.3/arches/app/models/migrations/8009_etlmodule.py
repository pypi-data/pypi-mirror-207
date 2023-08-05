# Generated by Django 2.2.24 on 2021-12-03 13:27

import re
import uuid
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
from arches.app.models.system_settings import settings

add_etl_manager = """
    insert into plugins (
        pluginid,
        name,
        icon,
        component,
        componentname,
        config,
        slug,
        sortorder)
    values (
        '7720e9fa-876c-4127-a77a-b099cd2a5d45',
        'ETL Manager',
        'fa fa-database',
        'views/components/plugins/etl-manager',
        'etl-manager',
        '{"show": false}',
        'etl-manager',
        2);
    """
remove_etl_manager = """
    delete from plugins where pluginid = '7720e9fa-876c-4127-a77a-b099cd2a5d45';
    """

add_csv_importer = """
    insert into etl_modules (
        etlmoduleid,
        name,
        description,
        etl_type,
        component,
        componentname,
        modulename,
        classname,
        config,
        icon,
        slug)
    values (
        '0a0cea7e-b59a-431a-93d8-e9f8c41bdd6b',
        'Import Single CSV',
        'Import a Single CSV file to Arches',
        'import',
        'views/components/etl_modules/import-single-csv',
        'import-single-csv',
        'import_single_csv.py',
        'ImportSingleCsv',
        '{"bgColor": "#9591ef", "circleColor": "#b0adf3", "show": true}',
        'fa fa-upload',
        'import-single-csv');
    """
remove_csv_importer = """
    delete from etl_modules where etlmoduleid = '0a0cea7e-b59a-431a-93d8-e9f8c41bdd6b';
    """

add_branch_csv_importer = """
    insert into etl_modules (
        etlmoduleid,
        name,
        description,
        etl_type,
        component,
        componentname,
        modulename,
        classname,
        config,
        icon,
        slug)
    values (
        '3b19a76a-0b09-450e-bee1-65accb096eaf',
        'Import Branch Excel',
        'Loads resource data in branch excel format',
        'import',
        'views/components/etl_modules/branch-csv-importer',
        'branch-csv-importer',
        'branch_csv_importer.py',
        'BranchCsvImporter',
        '{"circleColor": "#ff77cc", "bgColor": "#cc2266", "show": true}',
        'fa fa-upload',
        'branch-csv-importer'
    );
"""

remove_branch_csv_importer = """
    delete from etl_modules where etlmoduleid = '0a0cea7e-b59a-431a-93d8-e9f8c41bdd6b';
"""

add_validation_reporting_functions = """
    CREATE OR REPLACE FUNCTION public.__arches_load_staging_get_tile_errors(json_obj jsonb)
    RETURNS text
    LANGUAGE plpgsql AS

    $func$
    DECLARE
        _key   text;
        _value jsonb;
        _result text;
        _note text;

    BEGIN
        FOR _key, _value IN
            SELECT * FROM jsonb_each_text($1)
        LOOP
            IF _value ->> 'valid' = 'false' THEN
                IF _value ->> 'notes' IS NULL THEN
                    _note = 'unspecified error';
                END IF;
                -- we could add the nodeid (_key), but let's not be verbose just yet
                IF _result IS NULL THEN
                _result := _value ->> 'notes';
                ELSE
                _result := '|' || _value ->> 'notes';
                END IF;
            END IF;
        END LOOP;
        RETURN _result;
    END;
    $func$;

    CREATE OR REPLACE FUNCTION public.__arches_load_staging_report_errors(load_id uuid)
    RETURNS TABLE(source text, message text, loadid uuid)
    AS $$
        SELECT source_description, CONCAT_WS (' | ', public.__arches_load_staging_get_tile_errors(value), error_message) AS message, loadid
        FROM load_staging
        WHERE passes_validation IS NOT true
        AND loadid = load_id;
    $$ LANGUAGE SQL;

    CREATE OR REPLACE PROCEDURE public.__arches_check_tile_cardinality_violation_for_load(load_id uuid)
    AS $$
        UPDATE load_staging
            SET error_message = 'excess tile error', passes_validation = false
            WHERE loadid = load_id
			AND (resourceid, nodegroupid, COALESCE(parenttileid::text, '')) IN (
                SELECT t.resourceinstanceid, t.nodegroupid, COALESCE(t.parenttileid::text, '')
                    FROM tiles t, node_groups ng
                    WHERE t.nodegroupid = ng.nodegroupid
                    AND ng.cardinality = '1'
                UNION
                SELECT ls.resourceid, ls.nodegroupid, COALESCE(ls.parenttileid::text, '')
                    FROM load_staging ls, node_groups ng
                    WHERE ls.nodegroupid = ng.nodegroupid
                    AND ng.cardinality = '1'
                    GROUP BY ls.resourceid, ls.nodegroupid, COALESCE(ls.parenttileid::text, ''), ls.loadid
                    HAVING count(*) > 1
                    AND ls.loadid = load_id
            );
    $$ LANGUAGE SQL;
    """

remove_validation_reporting_functions = """
    DROP FUNCTION public.__arches_load_staging_get_tile_errors(json_obj jsonb);
    DROP FUNCTION public.__arches_load_staging_report_errors(load_id uuid);
    DROP PROCEDURE public.__arches_check_tile_cardinality_violation_for_load(load_id uuid)
    """

add_functions_to_get_nodegroup_tree = """
    CREATE OR REPLACE FUNCTION public.__get_nodegroup_tree(nodegroup_id uuid)
    RETURNS TABLE(nodegroupid uuid, parentnodegroupid uuid, alias text, name text, depth integer, path text, cardinality text)
    AS $$
    WITH RECURSIVE nodegroup_tree AS (
        SELECT
            nodegroupid,
            parentnodegroupid,
            alias,
            name,
            0 as depth,
            (select alias from nodes where nodeid = nodegroup_id) as path,
            cardinality
        FROM
        (SELECT ng.nodegroupid, ng.parentnodegroupid, alias, name, cardinality, graphid FROM node_groups ng
        INNER JOIN nodes n ON ng.nodegroupid = n.nodeid
        ORDER by ng.nodegroupid) AS root
        WHERE nodegroupid = nodegroup_id
        UNION
            SELECT
                parent.nodegroupid,
                parent.parentnodegroupid,
                parent.alias,
                parent.name,
                depth + 1,
                path || ' - ' || parent.alias,
                parent.cardinality
            FROM
            (SELECT ng.nodegroupid, ng.parentnodegroupid, alias, name, cardinality, graphid FROM node_groups ng
            INNER JOIN nodes n ON ng.nodegroupid = n.nodeid
            ORDER by ng.nodegroupid) AS parent
            INNER JOIN nodegroup_tree nt ON nt.nodegroupid = parent.parentnodegroupid
    ) SELECT
        *
    FROM
        nodegroup_tree order by path;
    $$
    LANGUAGE SQL;

    CREATE OR REPLACE FUNCTION public.__get_nodegroup_tree_by_graph(graph_id uuid)
    RETURNS TABLE(root_nodegroup uuid, nodegroupid uuid, parentnodegroupid uuid, alias text, name text, depth integer, path text, cardinality text)
    LANGUAGE PLPGSQL AS
    $func$
    DECLARE
    _nodegroupid uuid;
    BEGIN
    FOR _nodegroupid IN select ng.nodegroupid from node_groups ng join nodes n on ng.nodegroupid = nodeid where graphid = graph_id and ng.parentnodegroupid is null
    LOOP
        RETURN QUERY SELECT _nodegroupid, * FROM __get_nodegroup_tree(_nodegroupid);
    END LOOP;
    END;
    $func$;
    """

remove_functions_to_get_nodegroup_tree = [
    """
    DROP FUNCTION public.__get_nodegroup_tree(nodegroup_id uuid);
    DROP FUNCTION public.__get_nodegroup_tree_by_graph(graph_id uuid);
    """
]

add_staging_to_tile_function = """
    CREATE OR REPLACE FUNCTION public.__arches_staging_to_tile(load_id uuid)
    RETURNS BOOLEAN AS $$
        DECLARE
            status boolean;
            staged_value jsonb;
            tile_data jsonb;
            old_data jsonb;
            passed boolean;
            selected_resource text;
            graph_id uuid;
            instance_id uuid;
            legacy_id text;
            file_id uuid;
            tile_id uuid;
            parent_id uuid;
            nodegroup_id uuid;
            _file jsonb;
            _key text;
            _value text;
            tile_data_value jsonb;
            resource_object jsonb;
            resource_obejct_array jsonb;
        BEGIN
            FOR staged_value, instance_id, legacy_id, tile_id, parent_id, nodegroup_id, passed, graph_id IN
                    (
                        SELECT value, resourceid, legacyid, tileid, parenttileid, ls.nodegroupid, passes_validation, n.graphid
                        FROM load_staging ls INNER JOIN (SELECT DISTINCT nodegroupid, graphid FROM nodes) n
                        ON ls.nodegroupid = n.nodegroupid
                        WHERE loadid = load_id
                        ORDER BY nodegroup_depth ASC
                    )
                LOOP
                    IF passed THEN
                        SELECT resourceinstanceid FROM resource_instances INTO selected_resource WHERE resourceinstanceid = instance_id;
                        -- create a resource first if the rsource is not yet created
                        IF NOT FOUND THEN
                            INSERT INTO resource_instances(resourceinstanceid, graphid, legacyid, createdtime)
                                VALUES (instance_id, graph_id, legacy_id, now());
                            -- create resource instance edit log
                            INSERT INTO edit_log (resourceclassid, resourceinstanceid, edittype, timestamp, note, transactionid)
                                VALUES (graph_id, instance_id, 'create', now(), 'loaded from staging_table', load_id);
                        END IF;

                        -- create a tile one by one
                        tile_data := '{}'::jsonb;
                        FOR _key, _value IN SELECT * FROM jsonb_each_text(staged_value)
                            LOOP
                                tile_data_value = _value::jsonb -> 'value';
                                IF (_value::jsonb ->> 'datatype') in ('resource-instance-list', 'resource-instance') AND tile_data_value <> null THEN
                                    resource_obejct_array = '[]'::jsonb;
                                    FOR resource_object IN SELECT * FROM jsonb_array_elements(tile_data_value) LOOP
                                        resource_object = jsonb_set(resource_object, '{resourceXresourceId}', to_jsonb(uuid_generate_v1mc()));
                                        resource_obejct_array = resource_obejct_array || resource_object;
                                    END LOOP;
                                    tile_data_value = resource_obejct_array;
                                END IF;
                                tile_data = jsonb_set(tile_data, format('{"%s"}', _key)::text[], coalesce(tile_data_value, 'null'));
                            END LOOP;

                        SELECT tiledata FROM tiles INTO old_data WHERE resourceinstanceid = instance_id AND tileid = tile_id;
                        IF NOT FOUND THEN
                            old_data = null;
                        END IF;

                        INSERT INTO tiles(tileid, tiledata, nodegroupid, parenttileid, resourceinstanceid)
                            VALUES (tile_id, tile_data, nodegroup_id, parent_id, instance_id);
                        INSERT INTO edit_log (resourceclassid, resourceinstanceid, nodegroupid, tileinstanceid, edittype, newvalue, oldvalue, timestamp, note, transactionid)
                            VALUES (graph_id, instance_id, nodegroup_id, tile_id, 'tile create', tile_data::jsonb, old_data, now(), 'loaded from staging_table', load_id);
                    END IF;
                END LOOP;
            FOR staged_value, tile_id IN
                    (
                        SELECT value, tileid
                        FROM load_staging
                        WHERE loadid = load_id
                    )
                LOOP
                    FOR _key, _value IN SELECT * FROM jsonb_each_text(staged_value)
                        LOOP
                            CASE
                                WHEN (_value::jsonb ->> 'datatype') = 'file-list' THEN
                                    FOR _file IN SELECT * FROM jsonb_array_elements(_value::jsonb -> 'value') LOOP
                                        file_id = _file ->> 'file_id';
                                        UPDATE files SET tileid = tile_id WHERE fileid = file_id::uuid;
                                    END LOOP;
                                WHEN (_value::jsonb ->> 'datatype') in ('resource-instance-list', 'resource-instance') THEN
                                    PERFORM __arches_refresh_tile_resource_relationships(tile_id);
                                WHEN (_value::jsonb ->> 'datatype') = 'geojson-feature-collection' THEN
                                    PERFORM refresh_tile_geojson_geometries(tile_id);
                                ELSE
                            END CASE;
                        END LOOP;
                END LOOP;
            UPDATE load_event SET (load_end_time, complete, successful) = (now(), true, true) WHERE loadid = load_id;
            SELECT successful INTO status FROM load_event WHERE loadid = load_id;
            RETURN status;
        END;
    $$
    LANGUAGE plpgsql
    """

remove_staging_to_tile_function = """
    DROP FUNCTION public.__arches_staging_to_tile(load_id uuid);
    """

add_check_excess_tiles_trigger = """
    CREATE OR REPLACE FUNCTION __arches_check_excess_tiles_trigger_function()
    RETURNS trigger AS $$
    BEGIN
        IF (NEW.resourceinstanceid, NEW.nodegroupid, COALESCE(NEW.parenttileid::text, '')) IN (
                SELECT t.resourceinstanceid, t.nodegroupid, COALESCE(t.parenttileid::text, '')
                FROM tiles t, node_groups ng
                WHERE t.nodegroupid = ng.nodegroupid
                AND ng.cardinality = '1'
            ) THEN
                RAISE EXCEPTION 'Multiple Tiles for Cardinality-1 Nodegroup' USING ERRCODE = '21000';
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    CREATE TRIGGER __arches_check_excess_tiles_trigger
        BEFORE INSERT ON tiles
        FOR EACH ROW
        EXECUTE PROCEDURE __arches_check_excess_tiles_trigger_function();
    """

remove_check_excess_tiles_trigger = """
    DROP TRIGGER IF EXISTS __arches_check_excess_tiles_trigger ON tiles;
    DROP FUNCTION IF EXISTS __arches_check_excess_tiles_trigger_function()
    """


class Migration(migrations.Migration):

    dependencies = [
        ("models", "8042_3_spatialview_db_functions"),
    ]

    operations = [
        migrations.CreateModel(
            name="ETLModule",
            fields=[
                ("etlmoduleid", models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("description", models.TextField(blank=True, null=True)),
                ("etl_type", models.TextField()),
                ("component", models.TextField()),
                ("componentname", models.TextField()),
                ("modulename", models.TextField(blank=True, null=True)),
                ("classname", models.TextField(blank=True, null=True)),
                ("config", django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column="config", null=True)),
                ("icon", models.TextField()),
                (
                    "slug",
                    models.TextField(
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.",
                                "invalid",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "db_table": "etl_modules",
                "managed": True,
            },
        ),
        migrations.RunSQL(
            add_etl_manager,
            remove_etl_manager,
        ),
        migrations.RunSQL(
            add_csv_importer,
            remove_csv_importer,
        ),
        migrations.RunSQL(
            add_branch_csv_importer,
            remove_branch_csv_importer,
        ),
        migrations.CreateModel(
            name="LoadEvent",
            fields=[
                ("loadid", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("complete", models.BooleanField(default=False)),
                ("successful", models.BooleanField(blank=True, null=True)),
                ("status", models.TextField(blank=True, null=True)),
                ("etl_module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="models.ETLModule")),
                ("load_description", models.TextField(blank=True, null=True)),
                ("load_details", django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                ("load_start_time", models.DateTimeField(blank=True, null=True)),
                ("load_end_time", models.DateTimeField(blank=True, null=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "db_table": "load_event",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="LoadStaging",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column="value", null=True)),
                ("legacyid", models.TextField(blank=True, null=True)),
                ("resourceid", models.UUIDField(blank=True, null=True, serialize=False)),
                ("tileid", models.UUIDField(blank=True, null=True, serialize=False)),
                ("parenttileid", models.UUIDField(blank=True, null=True, serialize=False)),
                ("passes_validation", models.BooleanField(blank=True, null=True)),
                ("nodegroup_depth", models.IntegerField(default=1)),
                ("source_description", models.TextField(blank=True, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                (
                    "load_event",
                    models.ForeignKey(db_column="loadid", on_delete=django.db.models.deletion.CASCADE, to="models.LoadEvent"),
                ),
                (
                    "nodegroup",
                    models.ForeignKey(db_column="nodegroupid", on_delete=django.db.models.deletion.CASCADE, to="models.NodeGroup"),
                ),
            ],
            options={
                "db_table": "load_staging",
                "managed": True,
            },
        ),
        migrations.RunSQL(add_validation_reporting_functions, remove_validation_reporting_functions),
        migrations.RunSQL(add_functions_to_get_nodegroup_tree, remove_functions_to_get_nodegroup_tree),
        migrations.RunSQL(add_staging_to_tile_function, remove_staging_to_tile_function),
        migrations.RunSQL(add_check_excess_tiles_trigger, remove_check_excess_tiles_trigger),
    ]
