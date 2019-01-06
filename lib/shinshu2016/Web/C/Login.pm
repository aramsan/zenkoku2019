package shinshu2016::Web::C::Login;
use strict;
use warnings;
use utf8;

sub login {
    my ($class, $c) = @_;
    return $c->render('login.tx');
}

sub check {
    my ($class,$c) = @_;
    my $input = {
        email    => $c->crypt->encrypt_hex($c->req->param('email')),
        password => $c->crypt->encrypt_hex($c->req->param('password')),
    };
    my $entry = $c->db->single('entry', $input);
    if ($entry) {
        my $id = $entry->id;
        $c->session->set( 'login' => $id );
        $c->session->set( 'admin' => 1 ) if $entry->admin;
        return $c->redirect('/');
    } else {
        my $error = "メールアドレスかパスワードが間違っています。";
        return $c->render('login.tx', {
            error => $error,
        });
    }
}

sub logout {
    my ($class, $c) = @_;

    my $login = 0;
    $c->session->remove('login');
    $c->session->remove('admin');

    return $c->render('index.tx', {
        login => undef,
    });
}

1;
