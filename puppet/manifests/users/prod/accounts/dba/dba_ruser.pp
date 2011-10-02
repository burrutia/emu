class group::dba inherits group::dbavirtual {
        realize( Group[dba])
}
class user::dba inherits user::dbavirtual {
        realize( User[dba])
}

class user::dba_user1 inherits user::dbavirtual {
         realize( User[dba_user1])
}
