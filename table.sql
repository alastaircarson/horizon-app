create table viewpoint
(
	id serial primary key,
	geometry geometry(Point,27700),
	processed boolean default false,
	image_file character varying(50),
	peaks_file character varying(50)
);

create index viewpoint_sdx on viewpoint using gist (geometry);

insert into viewpoint(geometry, processed) values(ST_GeomFromText('POINT(279093 693777)',27700), false);
