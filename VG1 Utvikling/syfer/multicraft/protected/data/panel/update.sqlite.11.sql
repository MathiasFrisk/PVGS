alter table `server_config` add `user_jardir` integer not null default 0;
alter table `server_config` add `user_templates` integer not null default 1;
alter table `server_config` add `user_params` integer not null default 0;
update `config_file` set `options`='load:server_properties' where `options`='{"spawn-monsters":{"name":"Spawn Monsters","select":"bool"},"pvp":{"name":"Player vs Player","select":"bool"},"hellworld":{"name":"Hell World","select":"bool"},"online-mode":{"name":"Online Mode","select":"bool"},"spawn-animals":{"name":"Spawn Animals","select":"bool"},"server-ip":{"visible":false},"server-port":{"visible":false},"max-players":{"visible":false},"level-name":{"visible":false},"spawn-protection":{"name":"Protected Spawn Size","nocreate":true},"white-list":{"name":"Whitelisting","select":"bool"},"allow-nether":{"name":"Allow Nether","select":"bool"},"view-distance":{"name":"View Distance"},"level-seed":{"name":"Level Seed"},"allow-flight":{"name":"Allow Flying","select":"bool"},"gamemode":{"name":"Game Mode","select":{"0":"Survival","1":"Creative"}},"difficulty":{"name":"Difficulty","select":{"0":"Peaceful","1":"Easy","2":"Normal","3":"Hard"},"default":"1"},"motd":{"name":"Server Message"},"*":{"visible":true}}';
insert or ignore into `config_file` values(100,'Operators','List of users with operator access to the Minecraft server.','ops.json','','',1,'');
insert or ignore into `config_file` values(101,'Banned IPs','List of banned IP addresses for this server','banned-ips.json','','',1,'');
insert or ignore into `config_file` values(102,'Banned Players','List of banned player names for this server.','banned-players.json','','',1,'');
insert or ignore into `config_file` values(103,'Whitelisted Players','List of players that are allowed to connect. Note that this functionality is already provided by Multicraft.','white-list.json','','',1,'');
insert or ignore into `config_file` values(104,'Minecraft EULA','Accept the Minecraft EULA','eula.txt','load:minecraft_eula','properties',1,'');