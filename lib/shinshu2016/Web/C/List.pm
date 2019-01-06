package shinshu2016::Web::C::List;
use strict;
use warnings;
use utf8;

sub index {
    my ($class, $c) = @_;
    my $login = $c->session->get('login');
    my ($list, $pager) = $c->db->search_with_pager('entry',{ cancel => undef },{ order_by => { updated_on => 'desc'} , page => 1 , rows => 200 } );
    return $c->render('list.tx', {
        login => $login,
        list => $list,
        pager => $pager,
    });
}

1;
