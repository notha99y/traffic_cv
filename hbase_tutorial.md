# HBase Shell commands
## General Commands
```bash
status  'summary', 'simple', or 'detailed'
```
```bash
version
```
```bash
table_help
```
```bash
whoami
```

## Tables Management Commands
```bash
create <tablename>, <columnfamilyname>
```
```bash
list
```
```bash
describe <tablename>
```
```bash
disable <tablename>
# If table needs to be deleted or dropped, it has to disable first 
```
```bash
disable_all<"matching regex"
```
```bash
enable <tablename>
```
```bash
show_filters
# This command displays all the filters present in HBase like ColumnPrefix Filter, TimestampsFilter, PageFilter, FamilyFilter, etc.
```
```bash
drop <tablename>
```
```bash
drop_all<"regex">
```
```bash
is_enabled <tablename>
```