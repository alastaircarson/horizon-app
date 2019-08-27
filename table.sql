create table viewpoint
(
	id serial,
	geometry geometry(Point,27700),
	processed boolean default false,
	image_file character varying(50),
	peaks_file character varying(50)
);

create index viewpoint_sdx on viewpoint(geometry) using gist;
