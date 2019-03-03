package shinshu2016::DB::Schema;
use strict;
use warnings;
use utf8;

use Teng::Schema::Declare;

base_row_class 'shinshu2016::DB::Row';

table {
    name 'entry';
    pk 'id';
    columns qw(id name email password type grade departure adult child after after_adult after_child picture message cancel admin created_on updated_on);
};

1;
