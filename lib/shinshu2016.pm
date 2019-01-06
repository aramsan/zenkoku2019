package shinshu2016;
use strict;
use warnings;
use utf8;
our $VERSION='0.01';
use 5.008001;
use shinshu2016::DB::Schema;
use shinshu2016::DB;
use Cache::Redis;
use Crypt::CBC;

use parent qw/Amon2/;
# Enable project local mode.
__PACKAGE__->make_local_context();

my $schema = shinshu2016::DB::Schema->instance;

sub db {
    my $c = shift;
    if (!exists $c->{db}) {
        my $conf = $c->config->{DBI}
            or die "Missing configuration about DBI";
        $c->{db} = shinshu2016::DB->new(
            schema       => $schema,
            connect_info => [@$conf],
            # I suggest to enable following lines if you are using mysql.
            # on_connect_do => [
            #     'SET SESSION sql_mode=STRICT_TRANS_TABLES;',
            # ],
        );
    }
    $c->{db};
}

sub cache {
    my $c = shift;
    my $cache = Cache::Redis->new(
        server             => $c->config->{cache}{server}    || '127.0.0.1:6379',
        namespace          => $c->config->{cache}{namespace} || 'sinshu2016:',
        default_expires_in => $c->config->{cache}{expires}   || ( 60 * 60 * 24 * 30),    # 30日
    );
    no strict 'refs';
    *{ __PACKAGE__ . '::cache' } = sub {$cache};
}

sub crypt {
    my $c = shift;
    if (!exists $c->{crypt}) {
        my $conf = $c->config->{crypt}
            or die "Missing configratuion about Crypt";
        $c->{crypt} = Crypt::CBC->new(
            -key         => $conf->{key},
            -keysize     => 16,
            -literal_key => 1,
            -cipher      => "Rijndael",
            -iv          => '0000000000000000',
            -header      => 'none',
        );
    }
    $c->{crypt};
}

1;
__END__

=head1 NAME

shinshu2016 - shinshu2016

=head1 DESCRIPTION

This is a main context class for shinshu2016

=head1 AUTHOR

shinshu2016 authors.

