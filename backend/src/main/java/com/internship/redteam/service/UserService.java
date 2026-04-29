package com.internship.redteam.service;

import com.internship.redteam.entity.User;
import org.springframework.data.domain.Page;

public interface UserService {

    User createUser(User user);

    User getUserById(Long id);

    Page<User> getAllUsers(int page, int size);
}