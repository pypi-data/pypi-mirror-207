# Generated by Django 2.2.24 on 2022-05-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("models", "8403_bulk_index_queue"),
    ]

    operations = [
        migrations.RunSQL(
            """
            create or replace function __arches_tile_view_update() returns trigger as $$
                declare
                    view_namespace text;
                    group_id uuid;
                    graph_id uuid;
                    parent_id uuid;
                    tile_id uuid;
                    transaction_id uuid;
                    json_data json;
                    old_json_data jsonb;
                    edit_type text;
                begin
                    select graphid into graph_id from nodes where nodeid = group_id;
                    view_namespace = format('%s.%s', tg_table_schema, tg_table_name);
                    select obj_description(view_namespace::regclass, 'pg_class') into group_id;
                    if (TG_OP = 'DELETE') then
                        select tiledata into old_json_data from tiles where tileid = old.tileid;
                        delete from geojson_geometries where tileid = old.tileid;
                        delete from resource_x_resource where tileid = old.tileid;
                        delete from public.tiles where tileid = old.tileid;
                        insert into bulk_index_queue values (resourceinstanceid, current_timestamp) on conflict do nothing;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            nodegroupid,
                            tileinstanceid,
                            edittype,
                            oldvalue,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            graph_id,
                            old.resourceinstanceid,
                            group_id,
                            old.tileid,
                            'tile delete',
                            old_json_data,
                            now(),
                            'loaded via SQL backend',
                            public.uuid_generate_v1mc()
                        );
                        return old;
                    else
                        select __arches_get_json_data_for_view(new, tg_table_schema, tg_table_name) into json_data;
                        select __arches_get_parent_id_for_view(new, tg_table_schema, tg_table_name) into parent_id;
                        tile_id = new.tileid;
                        if (new.transactionid is null) then
                            transaction_id = public.uuid_generate_v1mc();
                        else
                            transaction_id = new.transactionid;
                        end if;

                        if (TG_OP = 'UPDATE') then
                            select tiledata into old_json_data from tiles where tileid = tile_id;
                            edit_type = 'tile edit';
                            if (transaction_id = old.transactionid) then
                                transaction_id = public.uuid_generate_v1mc();
                            end if;
                            update public.tiles
                            set tiledata = json_data,
                                nodegroupid = group_id,
                                parenttileid = parent_id,
                                resourceinstanceid = new.resourceinstanceid
                            where tileid = new.tileid;
                        elsif (TG_OP = 'INSERT') then
                            old_json_data = null;
                            edit_type = 'tile create';
                            if tile_id is null then
                                tile_id = public.uuid_generate_v1mc();
                            end if;
                            insert into public.tiles(
                                tileid,
                                tiledata,
                                nodegroupid,
                                parenttileid,
                                resourceinstanceid
                            ) values (
                                tile_id,
                                json_data,
                                group_id,
                                parent_id,
                                new.resourceinstanceid
                            );
                        end if;
                        perform refresh_tile_geojson_geometries(tile_id);
                        perform __arches_refresh_tile_resource_relationships(tile_id);
                        insert into bulk_index_queue values (resourceinstanceid, current_timestamp) on conflict do nothing;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            nodegroupid,
                            tileinstanceid,
                            edittype,
                            newvalue,
                            oldvalue,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            graph_id,
                            new.resourceinstanceid,
                            group_id,
                            tile_id,
                            edit_type,
                            json_data::jsonb,
                            old_json_data,
                            now(),
                            'loaded via SQL backend',
                            transaction_id
                        );
                        return new;
                    end if;
                end;
            $$ language plpgsql;

            create or replace function __arches_instance_view_update() returns trigger as $$
                declare
                    view_namespace text;
                    model_id uuid;
                    instance_id uuid;
                    transaction_id uuid;
                    edit_type text;
                begin
                    view_namespace = format('%s.%s', tg_table_schema, tg_table_name);
                    select obj_description(view_namespace::regclass, 'pg_class') into model_id;
                    if (TG_OP = 'DELETE') then
                        delete from public.resource_instances where resourceinstanceid = old.resourceinstanceid;
                        insert into bulk_index_queue values (resourceinstanceid, current_timestamp) on conflict do nothing;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            edittype,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            model_id,
                            old.resourceinstanceid,
                            'delete',
                            now(),
                            'loaded via SQL backend',
                            public.uuid_generate_v1mc()
                        );
                        return old;
                    else
                        instance_id = new.resourceinstanceid;
                        if instance_id is null then
                            instance_id = public.uuid_generate_v1mc();
                        end if;

                        if (new.transactionid is null) then
                            transaction_id = public.uuid_generate_v1mc();
                        else
                            transaction_id = new.transactionid;
                        end if;

                        if (TG_OP = 'UPDATE') then
                            edit_type = 'edit';
                            if (transaction_id = old.transactionid) then
                                transaction_id = public.uuid_generate_v1mc();
                            end if;
                            update public.resource_instances
                            set createdtime = new.createdtime,
                                legacyid = new.legacyid
                            where resourceinstanceid = instance_id;
                        elsif (TG_OP = 'INSERT') then
                            edit_type = 'create';
                            insert into public.resource_instances(
                                resourceinstanceid,
                                graphid,
                                legacyid,
                                createdtime
                            ) values (
                                instance_id,
                                model_id,
                                new.legacyid,
                                now()
                            );
                        end if;
                        insert into bulk_index_queue values (resourceinstanceid, current_timestamp) on conflict do nothing;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            edittype,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            model_id,
                            instance_id,
                            edit_type,
                            now(),
                            'loaded via SQL backend',
                            transaction_id
                        );
                        return new;
                    end if;
                end;
            $$ language plpgsql;
        """,
            """
            create or replace function __arches_tile_view_update() returns trigger as $$
                declare
                    view_namespace text;
                    group_id uuid;
                    graph_id uuid;
                    parent_id uuid;
                    tile_id uuid;
                    transaction_id uuid;
                    json_data json;
                    old_json_data jsonb;
                    edit_type text;
                begin
                    select graphid into graph_id from nodes where nodeid = group_id;
                    view_namespace = format('%s.%s', tg_table_schema, tg_table_name);
                    select obj_description(view_namespace::regclass, 'pg_class') into group_id;
                    if (TG_OP = 'DELETE') then
                        select tiledata into old_json_data from tiles where tileid = old.tileid;
                        delete from geojson_geometries where tileid = old.tileid;
                        delete from resource_x_resource where tileid = old.tileid;
                        delete from public.tiles where tileid = old.tileid;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            nodegroupid,
                            tileinstanceid,
                            edittype,
                            oldvalue,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            graph_id,
                            old.resourceinstanceid,
                            group_id,
                            old.tileid,
                            'tile delete',
                            old_json_data,
                            now(),
                            'loaded via SQL backend',
                            public.uuid_generate_v1mc()
                        );
                        return old;
                    else
                        select __arches_get_json_data_for_view(new, tg_table_schema, tg_table_name) into json_data;
                        select __arches_get_parent_id_for_view(new, tg_table_schema, tg_table_name) into parent_id;
                        tile_id = new.tileid;
                        if (new.transactionid is null) then
                            transaction_id = public.uuid_generate_v1mc();
                        else
                            transaction_id = new.transactionid;
                        end if;

                        if (TG_OP = 'UPDATE') then
                            select tiledata into old_json_data from tiles where tileid = tile_id;
                            edit_type = 'tile edit';
                            if (transaction_id = old.transactionid) then
                                transaction_id = public.uuid_generate_v1mc();
                            end if;
                            update public.tiles
                            set tiledata = json_data,
                                nodegroupid = group_id,
                                parenttileid = parent_id,
                                resourceinstanceid = new.resourceinstanceid
                            where tileid = new.tileid;
                        elsif (TG_OP = 'INSERT') then
                            old_json_data = null;
                            edit_type = 'tile create';
                            if tile_id is null then
                                tile_id = public.uuid_generate_v1mc();
                            end if;
                            insert into public.tiles(
                                tileid,
                                tiledata,
                                nodegroupid,
                                parenttileid,
                                resourceinstanceid
                            ) values (
                                tile_id,
                                json_data,
                                group_id,
                                parent_id,
                                new.resourceinstanceid
                            );
                        end if;
                        perform refresh_tile_geojson_geometries(tile_id);
                        perform __arches_refresh_tile_resource_relationships(tile_id);
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            nodegroupid,
                            tileinstanceid,
                            edittype,
                            newvalue,
                            oldvalue,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            graph_id,
                            new.resourceinstanceid,
                            group_id,
                            tile_id,
                            edit_type,
                            json_data::jsonb,
                            old_json_data,
                            now(),
                            'loaded via SQL backend',
                            transaction_id
                        );
                        return new;
                    end if;
                end;
            $$ language plpgsql;

            create or replace function __arches_instance_view_update() returns trigger as $$
                declare
                    view_namespace text;
                    model_id uuid;
                    instance_id uuid;
                    transaction_id uuid;
                    edit_type text;
                begin
                    view_namespace = format('%s.%s', tg_table_schema, tg_table_name);
                    select obj_description(view_namespace::regclass, 'pg_class') into model_id;
                    if (TG_OP = 'DELETE') then
                        delete from public.resource_instances where resourceinstanceid = old.resourceinstanceid;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            edittype,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            model_id,
                            old.resourceinstanceid,
                            'delete',
                            now(),
                            'loaded via SQL backend',
                            public.uuid_generate_v1mc()
                        );
                        return old;
                    else
                        instance_id = new.resourceinstanceid;
                        if instance_id is null then
                            instance_id = public.uuid_generate_v1mc();
                        end if;

                        if (new.transactionid is null) then
                            transaction_id = public.uuid_generate_v1mc();
                        else
                            transaction_id = new.transactionid;
                        end if;

                        if (TG_OP = 'UPDATE') then
                            edit_type = 'edit';
                            if (transaction_id = old.transactionid) then
                                transaction_id = public.uuid_generate_v1mc();
                            end if;
                            update public.resource_instances
                            set createdtime = new.createdtime,
                                legacyid = new.legacyid
                            where resourceinstanceid = instance_id;
                        elsif (TG_OP = 'INSERT') then
                            edit_type = 'create';
                            insert into public.resource_instances(
                                resourceinstanceid,
                                graphid,
                                legacyid,
                                createdtime
                            ) values (
                                instance_id,
                                model_id,
                                new.legacyid,
                                now()
                            );
                        end if;
                        insert into edit_log (
                            resourceclassid,
                            resourceinstanceid,
                            edittype,
                            timestamp,
                            note,
                            transactionid
                        ) values (
                            model_id,
                            instance_id,
                            edit_type,
                            now(),
                            'loaded via SQL backend',
                            transaction_id
                        );
                        return new;
                    end if;
                end;
            $$ language plpgsql;
        """,
        )
    ]
