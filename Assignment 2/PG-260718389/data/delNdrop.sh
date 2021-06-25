psql cs421 --echo-all <<-END 2>&1 | tee delNdrop.log

DROP TABLE host;
DROP TABLE participate;
DROP TABLE schedule;
DROP TABLE event;
DROP TABLE calendar;
DROP TABLE venue;
DROP TABLE organization;
DROP TABLE person;

END
