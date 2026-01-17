def count_valid_emails(emails):
    count = 0

    for email in emails:
        if isinstance(email, str) and email.count("@") == 1:
            local, domain = email.split("@")
            if local and domain:
                count += 1

    return count
