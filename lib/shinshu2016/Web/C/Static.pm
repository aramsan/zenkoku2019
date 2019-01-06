package shinshu2016::Web::C::Static;
use strict;
use warnings;
use utf8;

sub share {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('index.tx', {
        login => $login,
    });
}

sub gallery {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('gallery.tx', {
        login => $login,
    });
}

sub month3 {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('3month.tx', {
        login => $login,
    });
}

sub month2 {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('2month.tx', {
        login => $login,
    });
}

sub month1 {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('1month.tx', {
        login => $login,
    });
}

sub week2 {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('2week.tx', {
        login => $login,
    });
}

sub inquiry {
    my ($class, $c) = @_;

    my $login = $c->session->get('login');
    return $c->render('index.tx', {
        login => $login,
    });
}

1;
