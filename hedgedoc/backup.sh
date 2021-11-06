#!/bin/bash
docker-compose exec database pg_dump hedgedoc -U research > backup.sql
