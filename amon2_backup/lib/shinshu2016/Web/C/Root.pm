package shinshu2016::Web::C::Root;
use strict;
use warnings;
use utf8;

sub index {
    my ($class, $c) = @_;

    my $login = $c->session->get('login') ? 1 : undef;
    my $admin = $c->session->get('admin') ? 1 : undef;

    return $c->render('index.tx', {
        login => $login,
        admin => $admin,
    });
}

1;
