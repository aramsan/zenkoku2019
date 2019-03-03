package shinshu2016::Web::C::Admin;
use strict;
use warnings;
use utf8;

sub index {
    my ($class, $c) = @_;

    return $c->redirect('/') unless $c->session->get('admin');

    my @list = $c->db->search('entry');
    my $stats = $c->db->single_by_sql(q{SELECT count(id) AS total_num, sum(adult) AS total_adult, sum(child) as total_child, sum(after_adult) as total_after_adult, sum(after_child) as total_after_child FROM entry WHERE cancel is null})->get_columns;
    return $c->render('admin.tx', {
        list => \@list,
        stats => $stats,
    });
}

1;
